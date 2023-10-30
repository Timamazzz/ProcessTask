import BaseModelAPI from "../BaseModelAPI";
import apiConfig from "../apiConfig";
import axiosClient from "../axiosClient";
import { API_LIFESITUATION_MODEL } from "./const";

class LifesituationsApiRequest extends BaseModelAPI {
    constructor() {
        super(API_LIFESITUATION_MODEL.url);
    }

    async generateIdentifier<T>() {
        return this.makeRequest<T>(axiosClient.get, {method: API_LIFESITUATION_MODEL.methods.generateIdentifier.url});
    }
}

export default LifesituationsApiRequest;
