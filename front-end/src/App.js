import { useState, useCallback } from "react";
import axios from "axios";
import FormData from "form-data";
import "./App.css";

const App = () => {
  const [selectedFile, setSelectedFile] = useState();
  const [text, setText] = useState();
  const [blocks, setBlocks] = useState();

  const changeHandler = useCallback(
    (event) => {
      const file = event.target.files[0];
      file?.text().then((result) => {
        console.log("oh lala");
        setBlocks(null);
        setText(result);
      });
      setSelectedFile(file);
    },
    [setSelectedFile, setText, setBlocks]
  );

  const handleSubmission = useCallback(() => {
    const formData = new FormData();
    formData.append("receipt_doc", selectedFile);

    axios({
      method: "POST",
      url: "http://localhost:3000/receipts/",
      data: formData,
    })
      .then((response) => response.data)
      .then((result) => {
        setBlocks(result.blocks);
        console.log("Success:", result);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, [selectedFile, setBlocks]);

  const FONT_HEIGHT = 15.48;
  const FONT_WIDTH = 7.79;

  return (
    <div className="App">
      <div
        id="txt-show"
        style={{
          backgroundImage: text ? "" : `url("https://via.placeholder.com/500")`,
        }}
      >
        <div className="blocks-container">
          {blocks?.map((block) => (
            <div
              className="block"
              style={{
                top: block?.begin_row * FONT_HEIGHT,
                left: block?.begin_col * FONT_WIDTH,
                width: (block?.end_col - block?.begin_col) * FONT_WIDTH,
                height: (block?.end_row - block?.begin_row) * FONT_HEIGHT,
              }}
            />
          ))}
        </div>
        <pre id="txt-show-pre" class={text ? "initial" : "center"}>
          {text ? text : "Click Here to Upload Document"}
        </pre>
        <input
          type="file"
          id="file-upload"
          onChange={changeHandler}
          accept=".txt"
        />
        <label for="file-upload" id="txt-input"></label>
      </div>
      <button onClick={handleSubmission}>Analyze</button>
      {text && <h3>Click on the uploaded text to upload a new document</h3>}
    </div>
  );
};

export default App;
