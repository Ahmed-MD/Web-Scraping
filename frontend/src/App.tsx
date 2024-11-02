import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchQuestions } from './redux/actions';
import { RootState } from './redux/store';

const App: React.FC = () => {
  const [url, setUrl] = useState('');
  const dispatch = useDispatch();
  const { questions, loading, error } = useSelector((state: RootState) => state.questions);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    dispatch(fetchQuestions(url) as any);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Website Visitor Classification</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter website URL"
          className="border p-2 mr-2"
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          Analyze
        </button>
      </form>
      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">{error}</p>}
      {questions.length > 0 && (
        <div>
          <h2 className="text-xl font-bold mb-2">Questions:</h2>
          {questions.map((question, index) => (
            <div key={index} className="mb-4">
              <p className="font-semibold">{question.text}</p>
              <ul className="list-disc pl-6">
                {question.options.map((option, optionIndex) => (
                  <li key={optionIndex}>{option}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default App;