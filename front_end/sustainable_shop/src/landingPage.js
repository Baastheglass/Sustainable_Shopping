import React, { useEffect } from 'react';
import './landingPage.css';

function LandingPage() {
  useEffect(() => {
    const handleKeyDown = (event) => {
      if (event.code === 'Space') {
        // Simulate going to next page (you can replace this with React Router)
        window.location.href = '/nextpage'; // add next page here
      }
    };

    window.addEventListener('keydown', handleKeyDown);

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  return (
    <div className="landing-page">
      <div className="content">
        <h1 className="title">SnapShop</h1>
        <p className="slogan">Snap it. Find it. Buy it.</p>
        <p className="hint">(Press SPACEBAR to continue)</p>
      </div>
    </div>
  );
}

export default LandingPage;
