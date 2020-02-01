from typing import List

from pydantic import BaseModel


class ItemBase(BaseModel):
  title: str
  description: str = None


class ItemCreate(ItemBase):
  pass


class Item(ItemBase):
  id: int
  owner_id: int

  class Config:
    orm_mode = True


class UserBase(BaseModel):
  email: str


# 회원가입 시에만 패스워드가 필요
class UserCreate(UserBase):
  password: str


class User(UserBase):
  id: int
  is_active: bool
  items: List[Item] = []

  class Config:
    orm_mode = True


#### 학력사항 ####
class EducationBase(BaseModel):
  educationLevel: str  # 학력수준
  edcationDegree: str  # 대학원 석사 or 박사
  schoolName: str  # 학교 이름
  educationState: str  # 재학중, 졸업예정, 졸업
  majorCategory: str  # 주전공 계열
  majorName: str  # 주전공 이름
  hasMinor: bool = False  # 부/이중/복수 전공 여부
  minorName: str = ""  # 부전공 이름
  minorType: str = ""  # 부/이중/복수 전공 구분
  minorCategory: str = ""  # 부전공 계열
  schoolEntrance: str  # 입학일자(YYYYMM)
  schoolGraduation: str  # 졸업일자(YYYYMM)
  dayOrNight: str = "주간"  # 주간/야간 선택
  gpa: str  # 학점
  gpaScale: str  # 기준학점


class EducationCreate(EducationBase):
  pass


class Education(EducationBase):
  id: int
  resume_id = int

  class Config:
    orm_mode = True


#### 경력사항 ####

class CareerBase(BaseModel):
  companyName: str  # 회사 이름
  careerStart: str  # 입사일자(YYYYMM)
  careerEnd: str  # 퇴사일자(YYYYMM)
  companyLocation: str  # 회사 위치
  retired: bool  # 퇴사 or 재직중
  retireReason: str  # 퇴사이유
  jobGrade: str  # 직급
  jobDuty: str  # 직책
  jobCategory: str  # 직종
  jobDepartment: str  # 담당 부서
  jobContents: str  # 담당 업무


class CareerCreate(CareerBase):
  pass


class Career(CareerBase):
  id: int
  resume_id = int

  class Config:
    orm_mode = True

#### 자격증 ####


class LicenseBase(BaseModel):
  name: str  # 자격증명,
  publicOrg: str  # 발행기관
  obtainDate: str  # 획득일자


class LicenseCreate(LicenseBase):
  pass


class License(LicenseBase):
  id: int
  resume_id = int

  class Config:
    orm_mode = True

#### 어학 ####


class LanguageBase(BaseModel):
  language: str  # 언어
  examName: str  # 시험이름
  examScore: str  # 점수
  examLevel: str  # 급수, 리스트에 없는 값이면 에러
  examObtainDate: str  # 취득일자


class LanguageCreate(LanguageBase):
  pass


class Language(LanguageBase):
  id: int
  resume_id = int

  class Config:
    orm_mode = True

#### 채용플랫폼 계정정보 ####


class PlatformBase(BaseModel):
  site: str
  site_id: str
  site_pw: str


class PlatformCreate(PlatformBase):
  pass


class Platform(PlatformBase):
  id: int
  resume_id: int

  class Config:
    orm_mode = True

#### 이력서 데이터 ####


class ResumeCreate(BaseModel):
  platforms: List[PlatformCreate] = []
  educations: List[EducationCreate] = []
  careers: List[CareerCreate] = []
  licenses: List[LicenseCreate] = []
  languages: List[LanguageCreate] = []


class Resume(BaseModel):
  id: int

  platforms: List[Platform] = []
  educations: List[Education] = []
  careers: List[Career] = []
  licenses: List[License] = []
  languages: List[Language] = []

  class Config:
    orm_mode = True
