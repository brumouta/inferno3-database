import axios, {Options, RequestHeaders, Response} from 'redaxios';

const Api = axios.create();

Api.defaults.headers = {
  'Cache-Control': 'no-cache',
  'Pragma': 'no-cache',
  'Expires': '0',
};

const {get, post, put, delete: del, patch, request: req} = Api;

export {get, post, put, del, patch, req};
export type {Response, RequestHeaders, Options};
