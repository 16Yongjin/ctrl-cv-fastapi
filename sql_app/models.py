from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# 유저 모델
class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  hashed_password = Column(String)

  # platforms = relationship("Platform", back_populates="user")


# 이력서 모델
class Resume(Base):
  __tablename__ = "resumes"

  id = Column(Integer, primary_key=True, index=True)

  platforms = relationship("Education", back_populates="resume")
  educations = relationship("Education", back_populates="resume")
  careers = relationship("Career", back_populates="resume")
  licenses = relationship("License", back_populates="resume")
  languages = relationship("Language", back_populates="resume")


# 채용플랫폼 계정정보 모델
class Platform(Base):
  __tablename__ = "platforms"

  id = Column(Integer, primary_key=True, index=True)
  site = Column(String)
  site_id = Column(String)
  site_pw = Column(String)

  resume = relationship("Resume", back_populates="educations")

  # user = relationship("User", back_populates="platforms")


# 학력사항 모델
class Education(Base):
  __tablename__ = "educations"

  id = Column(Integer, primary_key=True, index=True)
  educationLevel = Column(String)  # 학력수준
  edcationDegree = Column(String)  # 대학원 석사 or 박사
  schoolName = Column(String)  # 학교 이름
  educationState = Column(String)  # 재학중, 졸업예정, 졸업
  majorCategory = Column(String)  # 주전공 계열
  majorName = Column(String)  # 주전공 이름
  hasMinor = Column(Boolean)  # 부/이중/복수 전공 여부
  minorName = Column(String)  # 부전공 이름
  minorType = Column(String)  # 부/이중/복수 전공 구분
  minorCategory = Column(String)  # 부전공 계열
  schoolEntrance = Column(String)  # 입학일자(YYYYMM)
  schoolGraduation = Column(String)  # 졸업일자(YYYYMM)
  dayOrNight = Column(String)  # 주간/야간 선택
  gpa = Column(String)  # 학점
  gpaScale = Column(String)  # 기준학점

  resume = relationship("Resume", back_populates="educations")


# 경력사항 모델
class Career(Base):
  __tablename__ = "careers"

  id = Column(Integer, primary_key=True, index=True)
  companyName = Column(String)  # 회사 이름
  careerStart = Column(String)  # 입사일자(YYYYMM)
  careerEnd = Column(String)  # 퇴사일자(YYYYMM)
  companyLocation = Column(String)  # 회사 위치
  retired = Column(Boolean)  # 퇴사 or 재직중
  retireReason = Column(String)  # 퇴사이유
  jobGrade = Column(String)  # 직급
  jobDuty = Column(String)  # 직책
  jobCategory = Column(String)  # 직종
  jobDepartment = Column(String)  # 담당 부서
  jobContents = Column(String)  # 담당 업무

  resume = relationship("Resume", back_populates="careers")


# 자격증 모델
class License(Base):
  __tablename__ = "licenses"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)  # 자격증명,
  publicOrg = Column(String)  # 발행기관
  obtainDate = Column(String)  # 획득일자

  resume = relationship("Resume", back_populates="licenses")


# 어학 모델
class Language(Base):
  __tablename__ = "languages"

  id = Column(Integer, primary_key=True, index=True)
  language = Column(String)  # 언어
  examName = Column(String)  # 시험이름
  examScore = Column(String)  # 점수
  examLevel = Column(String)  # 급수, 리스트에 없는 값이면 에러
  examObtainDate = Column(String)  # 취득일자

  resume = relationship("Resume", back_populates="languages")
