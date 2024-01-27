import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";

/*
This code renders our project so it can be viewed in a browser. 
*/

// document.getElementById("root") renders the index.html file that is the root file
ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
