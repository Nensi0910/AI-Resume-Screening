# ==========================================================
# AI-POWERED RESUME SCREENING SYSTEM
# Modern Light Professional UI
# ==========================================================

import streamlit as st
import pandas as pd

from styles import apply_styles

from utils import (
    save_resume,
    create_profile_summary,
    normalize_project_count
)

from resume_parser import (
    extract_resume_text,
    candidate_summary
)

from skill_extractor import (
    extract_skills,
    skill_match,
    categorize_skills
)

from ats import (
    generate_ats_report
)

from recommendation import (
    recommendation_report
)

from charts import (
    ats_gauge_chart,
    skill_match_chart,
    skill_category_chart,
    ats_component_chart
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# APPLY CUSTOM CSS
# ==========================================================

st.markdown(
    apply_styles(),
    unsafe_allow_html=True
)


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.divider()

    st.markdown(
        "### Candidate Analysis"
    )

    page = st.radio(
        "Select Analysis",
        [
            "Resume Parsing",
            "Skill Extraction",
            "ATS Scoring",
            "Candidate Ranking",
            "Improvement Suggestions",
            "Visualization",
        ],
        label_visibility="collapsed",
        key="analysis_page",
    )

    st.divider()

    st.caption(
        "AI Resume Screening System"
    )

    st.caption(
        "Automated candidate analysis"
    )


# ==========================================================
# MAIN HEADER
# ==========================================================

st.title(
    "AI-Powered Resume Screening System"
)

st.caption(
    "Intelligent resume analysis for faster and structured candidate screening."
)


# ==========================================================
# ANALYSIS INPUTS
# ==========================================================

upload_column, skills_column = st.columns(
    [1, 1.15],
    gap="large",
)

with upload_column:
    with st.container(border=True):
        st.subheader("📂 Upload resume")
        uploaded_file = st.file_uploader(
            "PDF, DOCX, or TXT",
            type=["pdf", "docx", "txt"],
            help="Supported formats: PDF, DOCX and TXT.",
            label_visibility="collapsed",
        )

with skills_column:
    with st.container(border=True):
        st.subheader("🎯 Job requirement skills")
        job_skills_input = st.text_input(
            "Required skills",
            placeholder="Python, SQL, Machine Learning, AWS",
            label_visibility="collapsed",
        )
        st.caption("Separate required skills with commas.")


# ==========================================================
# IF RESUME IS UPLOADED
# ==========================================================

if uploaded_file:

    # ======================================================
    # SAVE RESUME
    # ======================================================

    file_path = save_resume(
        uploaded_file
    )


    # ======================================================
    # EXTRACT RESUME
    # ======================================================

    with st.spinner(
        "Analyzing resume..."
    ):

        resume_text = extract_resume_text(
            uploaded_file
        )


    if resume_text == "":

        st.error(
            "Unable to read the uploaded resume."
        )

        st.stop()


    # ======================================================
    # CANDIDATE SUMMARY
    # ======================================================

    candidate = candidate_summary(
        resume_text
    )


    # ======================================================
    # SKILL EXTRACTION
    # ======================================================

    detected_skills = extract_skills(
        resume_text
    )


    # ======================================================
    # REQUIRED SKILLS
    # ======================================================

    if job_skills_input.strip():

        required_skills = [

            skill.strip()

            for skill in job_skills_input.split(",")

            if skill.strip()

        ]

    else:

        required_skills = detected_skills


    # ======================================================
    # SKILL MATCHING
    # ======================================================

    skill_analysis = skill_match(
        detected_skills,
        required_skills
    )


    # ======================================================
    # PROJECT COUNT
    # ======================================================

    project_value = candidate.get(
        "Projects",
        []
    )

    project_count = normalize_project_count(
        project_value
    )


    # ======================================================
    # ATS INPUT
    # ======================================================

    ats_input = {

        "skill_match":
            skill_analysis[
                "match_percentage"
            ],

        "experience":
            candidate.get(
                "Experience",
                0
            ),

        "education":
            candidate.get(
                "Education",
                []
            ),

        "certifications":
            candidate.get(
                "Certifications",
                []
            ),

        "projects":
            project_count

    }


    # ======================================================
    # ATS REPORT
    # ======================================================

    ats_result = generate_ats_report(
        ats_input
    )

    ats_score = ats_result[
        "ATS Score"
    ]


    # ======================================================
    # RECOMMENDATION
    # ======================================================

    recommendation = recommendation_report(

        ats_score,

        skill_analysis[
            "matched_skills"
        ],

        skill_analysis[
            "missing_skills"
        ],

        candidate.get(
            "Experience",
            0
        )

    )


    # ======================================================
    # PAGE 1 - RESUME PARSING
    # ======================================================

    if page == "Resume Parsing":

        st.header(
            "📄 Resume Parsing"
        )

        st.caption(
            "Candidate information extracted automatically from the uploaded resume."
        )


        profile = create_profile_summary(
            candidate
        )


        # --------------------------------------------------
        # TOP METRICS
        # --------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Candidate",
                profile[
                    "Candidate Name"
                ]
            )

        with col2:

            st.metric(
                "Experience",
                profile[
                    "Experience"
                ]
            )

        with col3:

            st.metric(
                "Projects",
                profile[
                    "Projects"
                ]
            )

        with col4:

            st.metric(
                "Certifications",
                len(
                    candidate.get(
                        "Certifications",
                        []
                    )
                )
            )


        st.divider()


        # --------------------------------------------------
        # CONTACT INFORMATION
        # --------------------------------------------------

        st.subheader(
            "👤 Candidate Information"
        )


        col1, col2 = st.columns(2)


        with col1:

            with st.container(border=True):

                st.caption(
                    "CANDIDATE NAME"
                )

                st.write(
                    profile[
                        "Candidate Name"
                    ]
                )


            with st.container(border=True):

                st.caption(
                    "EMAIL"
                )

                st.write(
                    profile[
                        "Email"
                    ]
                )


            with st.container(border=True):

                st.caption(
                    "PHONE"
                )

                st.write(
                    profile[
                        "Phone"
                    ]
                )


        with col2:

            with st.container(border=True):

                st.caption(
                    "EXPERIENCE"
                )

                st.write(
                    profile[
                        "Experience"
                    ]
                )


            with st.container(border=True):

                st.caption(
                    "EDUCATION"
                )

                st.write(
                    profile[
                        "Education"
                    ]
                )


            with st.container(border=True):

                st.caption(
                    "PROJECTS"
                )

                st.write(
                    profile[
                        "Projects"
                    ]
                )


        st.subheader(
            "🏆 Certifications"
        )


        with st.container(border=True):

            st.write(
                profile[
                    "Certifications"
                ]
            )


    # ======================================================
    # PAGE 2 - SKILL EXTRACTION
    # ======================================================

    elif page == "Skill Extraction":

        st.header(
            "🛠 Skill Extraction"
        )

        st.caption(
            "Technical skills automatically identified from the candidate resume."
        )


        # --------------------------------------------------
        # METRICS
        # --------------------------------------------------

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Total Skills",
                len(
                    detected_skills
                )
            )


        with col2:

            st.metric(
                "Matched Skills",
                len(
                    skill_analysis[
                        "matched_skills"
                    ]
                )
            )


        with col3:

            st.metric(
                "Missing Skills",
                len(
                    skill_analysis[
                        "missing_skills"
                    ]
                )
            )


        st.divider()


        # --------------------------------------------------
        # DETECTED SKILLS
        # --------------------------------------------------

        st.subheader(
            "Detected Skills"
        )


        if detected_skills:

            skill_df = pd.DataFrame(
                {
                    "Detected Skills":
                        sorted(
                            detected_skills
                        )
                }
            )


            st.dataframe(

                skill_df,

                use_container_width=True,

                hide_index=True

            )

        else:

            st.warning(
                "No skills detected."
            )


        st.write("")


        # --------------------------------------------------
        # MATCHED / MISSING
        # --------------------------------------------------

        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "✅ Matched Skills"
            )

            if skill_analysis[
                "matched_skills"
            ]:

                st.success(
                    ", ".join(
                        skill_analysis[
                            "matched_skills"
                        ]
                    )
                )

            else:

                st.info(
                    "No matched skills."
                )


        with col2:

            st.subheader(
                "⚠️ Missing Skills"
            )

            if skill_analysis[
                "missing_skills"
            ]:

                st.warning(
                    ", ".join(
                        skill_analysis[
                            "missing_skills"
                        ]
                    )
                )

            else:

                st.success(
                    "No missing skills."
                )


    # ======================================================
    # PAGE 3 - ATS SCORING
    # ======================================================

    elif page == "ATS Scoring":

        st.header(
            "📊 ATS Score Analysis"
        )

        st.caption(
            "Breakdown of the automated resume screening score."
        )


        # --------------------------------------------------
        # MAIN METRICS
        # --------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "ATS Score",
                f"{ats_score}%"
            )


        with col2:

            st.metric(
                "Skill Match",
                f"{skill_analysis['match_percentage']}%"
            )


        with col3:

            st.metric(
                "Matched Skills",
                len(
                    skill_analysis[
                        "matched_skills"
                    ]
                )
            )


        with col4:

            st.metric(
                "Missing Skills",
                len(
                    skill_analysis[
                        "missing_skills"
                    ]
                )
            )


        st.divider()


        # --------------------------------------------------
        # GAUGE + COMPONENTS
        # --------------------------------------------------

        st.subheader(
            "Overall ATS Score"
        )

        st.metric(
            label="Overall ATS Score",
            value=f"{ats_score}%",
            delta=None
        )

        st.plotly_chart(
            ats_gauge_chart(
                ats_score
            ),
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "ATS Components"
        )

        ats_df = pd.DataFrame(

            [

                [
                    "Skill Score",
                    ats_result.get(
                        "Skill Score",
                        0
                    )
                ],

                [
                    "Experience Score",
                    ats_result.get(
                        "Experience Score",
                        0
                    )
                ],

                [
                    "Education Score",
                    ats_result.get(
                        "Education Score",
                        0
                    )
                ],

                [
                    "Certification Score",
                    ats_result.get(
                        "Certification Score",
                        0
                    )
                ],

                [
                    "Project Score",
                    ats_result.get(
                        "Project Score",
                        0
                    )
                ],

                [
                    "ATS Score",
                    ats_result.get(
                        "ATS Score",
                        0
                    )
                ]

            ],

            columns=[
                "Component",
                "Score"
            ]

        )

        st.dataframe(
            ats_df,
            use_container_width=True,
            hide_index=True
        )


    # ======================================================
    # PAGE 4 - CANDIDATE RANKING
    # ======================================================

    elif page == "Candidate Ranking":

        st.header(
            "🏆 Candidate Evaluation"
        )

        st.caption(
            "Automated evaluation based on the configured ATS criteria."
        )


        # --------------------------------------------------
        # EXISTING LOGIC
        # --------------------------------------------------

        if ats_score >= 85:

            ranking = (
                "Excellent Candidate"
            )

            status = (
                "Strongly Recommended"
            )


        elif ats_score >= 70:

            ranking = (
                "Good Candidate"
            )

            status = (
                "Recommended"
            )


        else:

            ranking = (
                "Needs Improvement"
            )

            status = (
                "Not Recommended"
            )


        # --------------------------------------------------
        # STATUS
        # --------------------------------------------------

        with st.container(border=True):

            st.subheader(
                ranking
            )

            st.write(
                f"Current Hiring Status: **{status}**"
            )


        st.write("")


        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "ATS Score",
                f"{ats_score}%"
            )


        with col2:

            st.metric(
                "Hiring Status",
                status
            )


        st.divider()


        # --------------------------------------------------
        # HR RECOMMENDATION
        # --------------------------------------------------

        st.subheader(
            "HR Hiring Recommendation"
        )

        st.info(
            recommendation[
                "Decision"
            ]
        )


        st.subheader(
            "HR Feedback"
        )


        for feedback in recommendation[
            "HR Feedback"
        ]:

            with st.container(
                border=True
            ):

                st.write(
                    "• " + feedback
                )


    # ======================================================
    # PAGE 5 - IMPROVEMENT
    # ======================================================

    elif page == "Improvement Suggestions":

        st.header(
            "💡 Candidate Improvement Suggestions"
        )

        st.caption(
            "Recommendations for improving resume quality and job matching."
        )


        st.subheader(
            "Recommended Improvements"
        )


        for suggestion in recommendation[
            "Student Suggestions"
        ]:

            st.info(
                "💡 " + suggestion
            )


        st.divider()


        st.subheader(
            "Skills To Improve"
        )


        missing = skill_analysis[
            "missing_skills"
        ]


        if missing:

            st.warning(
                ", ".join(missing)
            )

        else:

            st.success(
                "Candidate has all required skills."
            )


    # ======================================================
    # PAGE 6 - VISUALIZATION
    # ======================================================

    elif page == "Visualization":

        st.header(
            "📈 Resume Analytics Dashboard"
        )

        st.caption(
            "Visual analysis of ATS performance and candidate skills."
        )


        # --------------------------------------------------
        # ATS SCORE
        # --------------------------------------------------

        st.subheader(
            "ATS Score"
        )

        st.plotly_chart(
            ats_gauge_chart(
                ats_score
            ),
            use_container_width=True
        )


        st.divider()


        # --------------------------------------------------
        # SKILL MATCH
        # --------------------------------------------------

        st.subheader(
            "Skill Match Analysis"
        )

        st.plotly_chart(

            skill_match_chart(

                skill_analysis[
                    "matched_skills"
                ],

                skill_analysis[
                    "missing_skills"
                ]

            ),

            use_container_width=True

        )


        st.divider()


        # --------------------------------------------------
        # SKILL CATEGORIES
        # --------------------------------------------------

        st.subheader(
            "Skill Category Distribution"
        )


        categories = categorize_skills(
            detected_skills
        )


        if categories:

            st.plotly_chart(

                skill_category_chart(
                    categories
                ),

                use_container_width=True

            )

        else:

            st.info(
                "No categorized skills available."
            )


        st.divider()


        # --------------------------------------------------
        # ATS COMPONENTS
        # --------------------------------------------------

        st.subheader(
            "ATS Component Analysis"
        )


        st.plotly_chart(

            ats_component_chart(
                ats_result
            ),

            use_container_width=True

        )


# ==========================================================
# NO RESUME UPLOADED
# ==========================================================

else:

    st.write("")

    with st.container(border=True):
        st.markdown("### 📄 Ready to analyze a resume?")
        st.caption(
            "Upload a candidate resume above to open the selected analysis page."
        )