import axios from 'axios';
import queryString from 'query-string';

import apiConfig from './apiConfig';
import { useTypeSelector } from '../hooks/useTypedSelector';

// const { token } = useTypeSelector((state) => state.authReducer);
const access = localStorage.getItem('access')

const axiosClient = axios.create({
    baseURL: apiConfig.baseUrl,
    headers: {
        ...(access  ? { 'Authorization': `Bearer ${access}` } : {}), // Установка заголовка авторизации при наличии токена
        'Content-Type': 'application/json'
    },
    paramsSerializer: params => queryString.stringify({ ...params, api_key: apiConfig.apiKey })
});

axiosClient.interceptors.request.use(async (config) => config);

axiosClient.interceptors.response.use((response) => {
    if (response && response.data) {
        return response.data;
    }

    return response;
}, (error) => {
    throw error;
});

export default axiosClient;
