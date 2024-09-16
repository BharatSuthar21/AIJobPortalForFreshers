import React from 'react';
import aboutData from '../data/About.json'; 
import '../styles/About.css';

const About = () => {
  return (
    <div className="about-container">
      <h1 className="about-title">About Us</h1>
      <p className="about-text">{aboutData.section1}</p>
      <p className="about-text">{aboutData.section2}</p>
      <p className="about-text">{aboutData.section3}</p>
    </div>
  );
};

export default About;
