import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-100 to-blue-300 p-6">
      <h1 className="text-5xl font-bold mb-10 text-blue-900 drop-shadow-md">Bienvenue sur OP Monitoring</h1>
      <div className="grid grid-cols-1 gap-8 w-full max-w-md">
        <Link
          to="/morning-check"
          className="block p-6 rounded-2xl bg-white shadow-lg hover:scale-105 hover:bg-blue-50 transition transform duration-300 text-center font-semibold text-xl text-blue-700"
        >
          📊 Morning Check
        </Link>
        <Link
          to="/functional-report"
          className="block p-6 rounded-2xl bg-white shadow-lg hover:scale-105 hover:bg-blue-50 transition transform duration-300 text-center font-semibold text-xl text-blue-700"
        >
          📈 Rapport Fonctionnel
        </Link>
      </div>
    </div>
  );
}

export default HomePage;
