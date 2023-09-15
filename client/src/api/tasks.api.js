import axios from 'axios'

// making base url for all api

const taskApi = axios.create({
    baseURL: 'http://localhost:8000/tasks/api/v1/task'
})

export const getAllTasks = () => taskApi.get('/');


export const createTask = (task) => taskApi.post('/', task);

export const deleteTask = (id) => taskApi.delete(`/${id}`)