import { useState, useEffect } from "react";
import Modal from 'react-modal';
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

  const [maxPreparationTime, setMaxPreparationTime] = useState(0);
  const [modalIsOpen, setModalIsOpen] = useState(false);

  const openModal = () => {
    setModalIsOpen(true);
  }
  const closeModal = () => {
    setModalIsOpen(false);
  }

  return (
    <div className="app">
      <h1>Customize your meal plan!</h1>

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

      <label for="slider">Maximum Preparation Time</label>
      <input type='range' min='0' max = '200' step='5' value={maxPreparationTime} onChange={(e)=>setMaxPreparationTime(e.target.value)} style={{ width: '40%' }} />
      <h6>{maxPreparationTime}</h6>

      <div className="generate-modal">
        <button onClick={openModal}>Generate!</button>
      </div>

      <div className="popup">
        <Modal
          isOpen={modalIsOpen}
          onRequestClose={closeModal}
          contentLabel="Generate Modal"
        >
            <div className="close-modal">
              <h2>Your Meal Plan</h2>
              <div className="meals-grid">
                <div className="box">
                  <h3>Breakfast</h3>
                </div>
                <div className="box">
                  <h3>Lunch</h3>
                </div>
                <div className="box">
                  <h3>Dinner</h3>
                </div>
                <div className="box">
                  <h3>Snacks</h3>
                </div>
              </div>
              <button onClick={closeModal}>Close</button>
            </div>
        </Modal>
      </div>
    </div> 
  );
}

export default App;
