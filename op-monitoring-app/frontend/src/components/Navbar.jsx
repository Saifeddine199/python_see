import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="p-4 shadow-md bg-white">
      <ul className="flex space-x-4">
        <li><Link to="/">Accueil</Link></li>
        {/* On ajoutera d'autres liens plus tard */}
      </ul>
    </nav>
  );
}

export default Navbar;