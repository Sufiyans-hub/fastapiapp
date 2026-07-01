import axios from "axios";
import type { Job } from "../types/job";

const API_BASE_URL = "http://localhost:5500";

export async function getJobs(): Promise<Job[]> {
    const response = await axios.get(`${API_BASE_URL}/jobs`);
    return response.data;
}

export async function getJob(id: string): Promise<Job> {
    const response = await axios.get(`${API_BASE_URL}/jobs/${id}`);
    return response.data;
}

export async function createJob(job: Job): Promise<Job> {
    const response = await axios.post(`${API_BASE_URL}/jobs`, job);
    return response.data;
}

export async function updateJob(id: string, job: Job): Promise<Job> {
    const response = await axios.put(`${API_BASE_URL}/jobs/${id}`, job);
    return response.data;
}

export async function deleteJob(id: string): Promise<Job> {
    const response = await axios.delete(`${API_BASE_URL}/jobs/${id}`);
    return response.data;
}