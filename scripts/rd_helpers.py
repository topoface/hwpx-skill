#!/usr/bin/env python3
"""
R&D 과제 신청서/보고서 특화 헬퍼 라이브러리.
정부지원사업 양식의 표준 컴포넌트(표지, 예산표, 일정표, 성과지표) 생성 함수를 제공한다.
"""
from hwpx_helpers import *

def make_rd_cover(project_name, org_name, pi_name, period):
    """R&D 과제 표준 표지 생성."""
    parts = []
    for _ in range(3): parts.append(make_empty_line())
    parts.append(make_cover_banner(project_name))
    for _ in range(2): parts.append(make_empty_line())
    parts.append(make_text_para(f"주관기관: {org_name}", charpr="62", parapr="52"))
    parts.append(make_text_para(f"연구책임자: {pi_name}", charpr="62", parapr="52"))
    parts.append(make_text_para(f"연구기간: {period}", charpr="60", parapr="1"))
    for _ in range(4): parts.append(make_empty_line())
    parts.append(make_page_break())
    return parts

def make_budget_table(direct, indirect, total):
    """연구비 구성 요약표 (단순화 버전)."""
    # 1행 3열 테이블 구조 (실제 구현 시 cell 추가)
    return make_section_bar("연구비", f"총 {total} (직접비 {direct}, 간접비 {indirect})")

def make_tech_section(title, content):
    """기술개발 내용 섹션 바 + 본문."""
    parts = []
    parts.append(make_section_bar("개발", title))
    parts.append(make_body_para("내용", content))
    return parts
