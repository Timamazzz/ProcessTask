import BaseModelAPI from "../BaseModelAPI";
import apiConfig from "../apiConfig";
import axiosClient from "../axiosClient";
import { API_SERVICES_MODEL } from "./const";

class ServicesApiRequest extends BaseModelAPI {
    constructor() {
        super(API_SERVICES_MODEL.url);
    }
}

export default ServicesApiRequest;
