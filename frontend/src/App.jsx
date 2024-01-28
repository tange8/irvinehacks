import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

/*
This is the starting point of our application. Here, we can begin coding 
and transforming this page into whatever best suits our needs. 
For example, we can start by creating a login page, home page, or an about section; 
there are many ways to get your application up and running. 
With App.jsx, we can also define global variables and routes to store information as well as page navigation.
*/
const dietaryChoices = [
  {label: 'Anything', img: "/icons/icon-bento.png"},
  {label: 'Vegan', img: "/icons/icon-vegan.png"},
  {label: 'Vegetarian', img: "/icons/icon-vegetarian.png"},
  {label: 'Paleo', img: "/icons/icon-paleo.png"},
  {label: 'Dairy-Free', img: "/icons/icon-dairy-free.png"},
  {label: 'Sugar-Free', img: "/icons/icon-sugar-free.png"},
  {label: 'Low Sodium', img: "/icons/icon-low-salt.png"},
  {label: 'No Fish', img: "/icons/icon-no-fish.png"},
];

function App() {
  const [selectedChoices, setSelectedChoices] = useState([]);

  const handleSelect = (label) => {
    if (selectedChoices.includes(label)) {
      setSelectedChoices(selectedChoices.filter((choice) => choice !== label));
    } else {
      setSelectedChoices([...selectedChoices, label]);
    }
  };

  return (
    <div className="app">
      <div className="choice-grid"> 
        {dietaryChoices.map((choice) => (
          <div
            // key attribute is set to the label property of each choice object
            key={choice.label}
            // checks if selectedChoices array includes choice.label
            // if it does, it adds the class "selected" to the class name
            // if it doesn't, it adds an empty string
            className={`choice-box ${selectedChoices.includes(choice.label) ? 'selected' : ''}`}
            onClick={() => handleSelect(choice.label)}>
              <div className="choice-icon">{choice.icon}
                <img src={choice.img} alt={choice.label} />
              </div>
              <div className="choice-label">{choice.label}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
