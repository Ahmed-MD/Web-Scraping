// actions.ts
import { Dispatch } from 'redux';
import axios from 'axios';
import { ThunkAction } from 'redux-thunk';
import { RootState } from './store';

export const FETCH_QUESTIONS_REQUEST = 'FETCH_QUESTIONS_REQUEST';
export const FETCH_QUESTIONS_SUCCESS = 'FETCH_QUESTIONS_SUCCESS';
export const FETCH_QUESTIONS_FAILURE = 'FETCH_QUESTIONS_FAILURE';

interface Question {
  text: string;
  options: string[];
}

export const fetchQuestions = (url: string): ThunkAction<void, RootState, unknown, QuestionsAction> => {
  return async (dispatch: Dispatch<QuestionsAction>) => {
    dispatch({ type: FETCH_QUESTIONS_REQUEST });
    try {
      const response = await axios.post('http://localhost:5000/scrape', { url });
      dispatch({
        type: FETCH_QUESTIONS_SUCCESS,
        payload: response.data,
      });
    } 
    catch (error) {
      // dispatch({
      //   // type: FETCH_QUESTIONS_FAILURE,
      //   // payload: error.message,
      // });
    }
  };
};

export type QuestionsAction =
  | { type: typeof FETCH_QUESTIONS_REQUEST }
  | { type: typeof FETCH_QUESTIONS_SUCCESS; payload: Question[] }
  | { type: typeof FETCH_QUESTIONS_FAILURE; payload: string };
