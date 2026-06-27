from fastapi import APIRouter
from schemas.job import JobCreate,JobUpdate 
router = APIRouter(prefix="/job", tags=["job"] )

jobs = []

@router.post("/")
def create_jobs(company: JobCreate):
    jobs.append(company)
    return jobs

@router.get("/")
def get_all_job():
    return jobs

@router.get("/{job_id}")
def get_job(job_id:int):
    return jobs[job_id]

@router.put("/{company_id}")
def update_company(company_id:int,company: JobUpdate):
    jobs[company_id] = company
    return jobs
@router.delete("/{company_id}")
def delete_company(company_id:int):
    jobs.pop(company_id)
    return jobs


# @router.get('/')
# def read_job():
#     return {'job':"Job Done"}

# @router.get("/job_id")
# def read_job(job_id:int):
#     return {"job_id":job_id}