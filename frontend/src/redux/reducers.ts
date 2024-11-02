// reducers.ts
import { AnyAction } from 'redux';
import { FETCH_QUESTIONS_REQUEST, FETCH_QUESTIONS_SUCCESS, FETCH_QUESTIONS_FAILURE, QuestionsAction } from './actions';

interface Question {
  text: string;
  options: string[];
}

interface QuestionsState {
  loading: boolean;
  questions: Question[];
  error: string | null;
}

const initialState: QuestionsState = {
  loading: false,
  questions: [],
  error: null,
};

// Type guard to check action types
const isFetchQuestionsRequest = (action: AnyAction): action is { type: typeof FETCH_QUESTIONS_REQUEST } =>
  action.type === FETCH_QUESTIONS_REQUEST;

const isFetchQuestionsSuccess = (action: AnyAction): action is { type: typeof FETCH_QUESTIONS_SUCCESS; payload: Question[] } =>
  action.type === FETCH_QUESTIONS_SUCCESS;

const isFetchQuestionsFailure = (action: AnyAction): action is { type: typeof FETCH_QUESTIONS_FAILURE; payload: string } =>
  action.type === FETCH_QUESTIONS_FAILURE;

const questionsReducer = (state = initialState, action: AnyAction): QuestionsState => {
  if (isFetchQuestionsRequest(action)) {
    return { ...state, loading: true, error: null };
  }
  if (isFetchQuestionsSuccess(action)) {
    return { ...state, loading: false, questions: action.payload };
  }
  if (isFetchQuestionsFailure(action)) {
    return { ...state, loading: false, error: action.payload };
  }
  return state;
};

export default questionsReducer;
