import axios, {Options, RequestHeaders, Response} from 'redaxios';

const Api = axios.create();

const { get, post, put, delete: del, patch: patch, request: req} = Api;

export { get, post, put, del, patch, req };
export type { Response, RequestHeaders, Options };