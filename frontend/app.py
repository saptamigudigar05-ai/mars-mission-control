import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import random

BACKEND_URL = "http://127.0.0.1:8000"

def get_mission_status():
    try:
        response = requests.get(
            f"{BACKEND_URL}/api/status/",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None

mission_data = get_mission_status()
if mission_data:
    mission_status = mission_data.get("status", "UNKNOWN")
    oxygen_status = mission_data.get("oxygen", "UNKNOWN")
    communication_status = mission_data.get("communication", "UNKNOWN")
    astra_signal = mission_data.get("astra_signal", "UNKNOWN")
else:
    mission_status = "OFFLINE"
    oxygen_status = "UNKNOWN"
    communication_status = "UNKNOWN"
    astra_signal = "UNKNOWN"

st.subheader("🔌 Backend Connection")

try:
    response = requests.get(
        f"{BACKEND_URL}/api/status/",
        timeout=5
    )

    if response.status_code == 200:
        data = response.json()

        st.success("🟢 Django Backend Connected!")
        st.json(data)

    else:
        st.error(
            f"🔴 Backend returned status code: {response.status_code}"
        )

except requests.exceptions.RequestException as e:
    st.error(f"🔴 Backend connection failed: {e}")

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ASTRA-1 Mission Control",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* ---------- MAIN APP ---------- */

.stApp {
    background:
        radial-gradient(circle at 50% 30%, #111a38 0%, #050914 45%, #02040a 100%);
    color: white;
}

/* ---------- STARS ---------- */

.star {
    position: fixed;
    width: 3px;
    height: 3px;
    background: white;
    border-radius: 50%;
    z-index: 0;
    pointer-events: none;
}

.star1 {
    left: 5%;
    top: 10%;
    animation: starMove1 8s linear infinite;
}

.star2 {
    left: 15%;
    top: 50%;
    animation: starMove2 12s linear infinite;
}

.star3 {
    left: 30%;
    top: 20%;
    animation: starMove3 10s linear infinite;
}

.star4 {
    left: 45%;
    top: 70%;
    animation: starMove4 15s linear infinite;
}

.star5 {
    left: 60%;
    top: 15%;
    animation: starMove5 9s linear infinite;
}

.star6 {
    left: 75%;
    top: 45%;
    animation: starMove6 13s linear infinite;
}

.star7 {
    left: 90%;
    top: 20%;
    animation: starMove7 11s linear infinite;
}

.star8 {
    left: 80%;
    top: 80%;
    animation: starMove8 14s linear infinite;
}

@keyframes starMove1 {
    0% { transform: translateY(-100px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(700px); opacity: 0; }
}

@keyframes starMove2 {
    0% { transform: translateY(-200px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(800px); opacity: 0; }
}

@keyframes starMove3 {
    0% { transform: translateY(-300px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(900px); opacity: 0; }
}

@keyframes starMove4 {
    0% { transform: translateY(-400px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(900px); opacity: 0; }
}

@keyframes starMove5 {
    0% { transform: translateY(-200px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(800px); opacity: 0; }
}

@keyframes starMove6 {
    0% { transform: translateY(-150px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(700px); opacity: 0; }
}

@keyframes starMove7 {
    0% { transform: translateY(-250px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(850px); opacity: 0; }
}

@keyframes starMove8 {
    0% { transform: translateY(-350px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(900px); opacity: 0; }
}


/* ---------- ROCKET ---------- */

.rocket {
    position: fixed;
    top: 15%;
    left: -100px;
    font-size: 45px;
    z-index: 1;
    pointer-events: none;

    animation: rocketFlight 18s linear infinite;
}

@keyframes rocketFlight {

    0% {
        left: -100px;
        transform: rotate(0deg);
    }

    45% {
        left: 45%;
        transform: rotate(5deg);
    }

    100% {
        left: 110%;
        transform: rotate(0deg);
    }

}


/* ---------- MARS ---------- */

.mars {
    position: fixed;

    right: 35px;
    bottom: 45px;

    width: 170px;
    height: 170px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            #ffbd78 0%,
            #e66b3c 30%,
            #9b3828 65%,
            #421515 100%
        );

    box-shadow:
        0 0 25px rgba(255, 80, 40, 0.5),
        0 0 70px rgba(255, 50, 30, 0.25);

    z-index: 0;

    animation: marsFloat 5s ease-in-out infinite;
}

@keyframes marsFloat {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-25px);
    }

    100% {
        transform: translateY(0px);
    }

}


/* ---------- CONTENT ---------- */

.block-container {
    position: relative;
    z-index: 5;
}


/* ---------- HEADER ---------- */

.main-title {
    text-align: center;

    font-size: 42px;
    font-weight: 800;

    letter-spacing: 4px;

    color: white;

    text-shadow:
        0 0 10px #4db8ff,
        0 0 25px #4db8ff;
}

.subtitle {
    text-align: center;

    color: #9db7d4;

    letter-spacing: 2px;

    margin-bottom: 25px;
}


/* ---------- CARDS ---------- */

.card {
    background: rgba(8, 15, 32, 0.92);

    border: 1px solid rgba(77, 184, 255, 0.25);

    border-radius: 15px;

    padding: 20px;

    margin-bottom: 20px;

    box-shadow:
        0 0 20px rgba(0, 140, 255, 0.08);

    backdrop-filter: blur(10px);
}

.card:hover {
    border-color: rgba(77, 184, 255, 0.7);

    box-shadow:
        0 0 30px rgba(77, 184, 255, 0.15);
}


/* ---------- STATUS CARDS ---------- */

.status-card {

    background: rgba(8, 15, 32, 0.95);

    border: 1px solid rgba(255,255,255,0.1);

    border-radius: 12px;

    padding: 18px;

    text-align: center;

    min-height: 100px;
}

.status-title {

    color: #8298b2;

    font-size: 11px;

    letter-spacing: 1px;
}

.status-value {

    font-size: 21px;

    font-weight: bold;

    margin-top: 10px;
}

.critical {
    color: #ff4d5a;
}

.warning {
    color: #ffb84d;
}

.good {
    color: #4dff9a;
}

.info {
    color: #4db8ff;
}


/* ---------- LIVE ---------- */

.live {

    color: #ff4d5a;

    font-weight: bold;

    animation: blink 1.2s infinite;
}

@keyframes blink {

    50% {
        opacity: 0.3;
    }

}


/* ---------- RADAR ---------- */

.radar {

    width: 250px;
    height: 250px;

    margin: 25px auto;

    border-radius: 50%;

    border: 2px solid rgba(0,255,130,0.6);

    background:
        radial-gradient(
            circle,
            transparent 19%,
            rgba(0,255,130,0.08) 20%,
            transparent 21%
        ),
        radial-gradient(
            circle,
            transparent 39%,
            rgba(0,255,130,0.08) 40%,
            transparent 41%
        ),
        radial-gradient(
            circle,
            transparent 59%,
            rgba(0,255,130,0.08) 60%,
            transparent 61%
        );

    position: relative;

    overflow: hidden;
}

.radar::after {

    content: "";

    position: absolute;

    width: 50%;

    height: 2px;

    top: 50%;
    left: 50%;

    background: #00ff88;

    transform-origin: left center;

    animation: radarScan 3s linear infinite;

    box-shadow: 0 0 15px #00ff88;
}

@keyframes radarScan {

    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }

}


/* ---------- FOOTER ---------- */

.footer {

    text-align: center;

    margin-top: 40px;

    padding: 20px;

    color: #61758d;

    font-size: 11px;

    letter-spacing: 1px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# ANIMATED SPACE
# =========================================================

st.markdown("""
<div class="star star1"></div>
<div class="star star2"></div>
<div class="star star3"></div>
<div class="star star4"></div>
<div class="star star5"></div>
<div class="star star6"></div>
<div class="star star7"></div>
<div class="star star8"></div>

<div class="rocket">🚀</div>

<div class="mars"></div>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("# 🚀 ASTRA-1")

    st.caption("MARS MISSION CONTROL")

    st.divider()

    page = st.radio(
        "MISSION MODULES",
        [
            "🚨 Mission Overview",
            "🪐 Mission Briefing",
            "🤖 Robot Operations",
            "🏥 Emergency Triage",
            "📡 Communications",
            "🧠 Mission Recommendation"
        ]
    )

    st.divider()

    st.markdown("### SYSTEM STATUS")

    st.markdown(
        '<p class="live">● LIVE SYSTEM</p>',
        unsafe_allow_html=True
    )

    st.write("🛰️ Network: DEGRADED")
    st.write("🤖 Robots: 3 ONLINE")
    st.write("🫁 Oxygen: CRITICAL")


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🚀 ASTRA-1 MISSION CONTROL</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">MARS COLONY EMERGENCY OPERATIONS DASHBOARD</div>',
    unsafe_allow_html=True
)

st.info(
    "⚠️ PROTOTYPE SYSTEM — Simulated mission data for demonstration."
)


# =========================================================
# MISSION OVERVIEW
# =========================================================

if page == "🚨 Mission Overview":

    st.subheader("🚨 Mission Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown("""
        <div class="status-card">

        <div class="status-title">
        MISSION STATUS
        </div>

        <div class="status-value critical">
        CRITICAL
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="status-card">

        <div class="status-title">
        OXYGEN PRODUCTION
        </div>

        <div class="status-value critical">
        DEGRADED
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="status-card">

        <div class="status-title">
        COMMUNICATIONS
        </div>

        <div class="status-value warning">
        DISRUPTED
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown("""
        <div class="status-card">

        <div class="status-title">
        AUTONOMOUS SYSTEMS
        </div>

        <div class="status-value critical">
        FAILING
        </div>

        </div>
        """, unsafe_allow_html=True)


    st.write("")


    # Mission metrics

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Mission Window",
            "06:00:00",
            "Active"
        )

    with col2:
        st.metric(
            "Colony Population",
            "10,000",
            "At Risk"
        )

    with col3:
        st.metric(
            "Mission Risk",
            "HIGH",
            "↑"
        )


    st.divider()


    # Tactical situation + radar

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <h3>📡 Tactical Situation</h3>

        <p>🛰️ <b>ASTRA-1:</b> Signal Lost</p>

        <p>❓ <b>Unknown Signal:</b> Detected</p>

        <p>🤖 <b>ROVER-01:</b> Operational</p>

        <p>⚠️ <b>Colony Network:</b> Unstable</p>

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="card">

        <h3>📡 Mars Radar</h3>

        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            '<div class="radar"></div>',
            unsafe_allow_html=True
        )

        st.caption(
            "Scanning Mars communication zone..."
        )


    # Intelligence

    st.markdown("""
    <div class="card">

    <h3>🧠 Mission Intelligence</h3>

    <p>
    Communication recovery should be prioritized while
    deploying a relay-capable rover and continuing the
    ASTRA-1 search.
    </p>

    </div>
    """, unsafe_allow_html=True)


    # Telemetry

    st.subheader("📈 Live Mission Telemetry")

    telemetry = pd.DataFrame({

        "Oxygen": [
            100,
            96,
            91,
            84,
            77,
            70
        ],

        "Communication": [
            100,
            94,
            86,
            70,
            58,
            45
        ]

    })

    st.line_chart(telemetry)


# =========================================================
# MISSION BRIEFING
# =========================================================

elif page == "🪐 Mission Briefing":

    st.subheader("🪐 Mission Briefing")

    st.markdown("""
    <div class="card">

    <h2>🎯 Mission Objective</h2>

    <p>
    Maintain Mars colony survival by continuously monitoring
    critical systems, analyzing incoming data and prioritizing
    emergency actions.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.subheader("🔄 Autonomous Decision Workflow")

    cols = st.columns(5)

    workflow = [
        ("1", "SENSE"),
        ("2", "ANALYZE"),
        ("3", "PRIORITIZE"),
        ("4", "ACT"),
        ("5", "ADAPT")
    ]

    for col, item in zip(cols, workflow):

        with col:

            number, name = item

            st.markdown(
                f"""
                <div class="card" style="text-align:center">

                <h2>{number}</h2>

                <b>{name}</b>

                </div>
                """,
                unsafe_allow_html=True
            )


    st.markdown("""
    <div class="card">

    <h3>🚨 Crisis Sequence</h3>

    <p>1️⃣ Detect abnormal system behavior</p>
    <p>2️⃣ Analyze mission telemetry</p>
    <p>3️⃣ Identify critical threats</p>
    <p>4️⃣ Prioritize emergency actions</p>
    <p>5️⃣ Dispatch autonomous systems</p>
    <p>6️⃣ Continuously reassess conditions</p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ROBOT OPERATIONS
# =========================================================

elif page == "🤖 Robot Operations":

    st.subheader("🤖 Robot Operations")
    
    st.subheader("🚀 Robot Command Center")

robot = st.selectbox(
    "Select Robot",
    ["ROVER-01", "ROVER-02", "DRONE-01"]
)

command = st.selectbox(
    "Select Command",
    [
        "SCAN AREA",
        "MOVE TO ASTRA",
        "DEPLOY RELAY",
        "RETURN TO BASE"
    ]
)

if st.button("🚀 SEND COMMAND"):
    try:
        response = requests.post(
            f"{BACKEND_URL}/api/robot-command/",
            json={
                "robot": robot,
                "command": command
            },
            timeout=5
        )

        if response.status_code == 200:
            st.success("🟢 Command sent successfully!")
            st.json(response.json())
        else:
            st.error(f"🔴 Command failed: {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"🔴 Backend connection failed: {e}")
    robot_data = pd.DataFrame({

        "Robot": [
            "ROVER-01",
            "ROVER-02",
            "DRONE-01"
        ],

        "Status": [
            "ONLINE",
            "ONLINE",
            "STANDBY"
        ],

        "Battery": [
            "87%",
            "64%",
            "91%"
        ],

        "Mission": [
            "Relay Deployment",
            "Colony Patrol",
            "Aerial Survey"
        ]

    })

    st.dataframe(
        robot_data,
        use_container_width=True,
        hide_index=True
    )


    st.divider()


    st.subheader("🎮 Command Center")

    col1, col2 = st.columns(2)

    with col1:

        selected_robot = st.selectbox(
            "Select Robot",
            ["ROVER-01", "ROVER-02", "DRONE-01"],
            key="robot_selector"
        )

    with col2:

        command = st.selectbox(
            "Select Command",
            [
                "MOVE TO LOCATION",
                "DEPLOY COMMUNICATION RELAY",
                "SCAN AREA",
                "RETURN TO BASE",
                "START SURVEY"
            ]
        )


    if st.button("🚀 SEND COMMAND"):

        st.success(
            f"Command '{command}' sent to {selected_robot}"
        )


    st.markdown("""
    <div class="card">

    <h3>🤖 Autonomous Operations</h3>

    <p>
    Robots continuously report battery, location,
    mission status and environmental conditions to
    Mission Control.
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# EMERGENCY TRIAGE
# =========================================================

elif page == "🏥 Emergency Triage":

    st.subheader("🏥 Emergency Triage")

    triage_data = pd.DataFrame({

        "Case": [
            "CASE-001",
            "CASE-002",
            "CASE-003",
            "CASE-004"
        ],

        "Priority": [
            "CRITICAL",
            "HIGH",
            "MEDIUM",
            "LOW"
        ],

        "Location": [
            "Habitat A",
            "Habitat B",
            "Research Lab",
            "Storage Zone"
        ],

        "Response": [
            "Immediate",
            "Within 10 min",
            "Within 30 min",
            "Monitor"
        ]

    })

    st.dataframe(
        triage_data,
        use_container_width=True,
        hide_index=True
    )


    st.divider()


    st.subheader("🧠 Triage Logic")

    st.markdown("""
    <div class="card">

    <p>
    Emergency cases are prioritized using:
    </p>

    <p>🔴 Severity</p>
    <p>📍 Location</p>
    <p>⏱️ Response time</p>
    <p>🧰 Available resources</p>
    <p>👥 Number of people affected</p>

    </div>
    """, unsafe_allow_html=True)

st.subheader("🚨 Emergency Case Recording")

patient = st.text_input("Patient / Crew ID")

severity = st.selectbox(
    "Severity",
    ["CRITICAL", "HIGH", "MEDIUM", "LOW"],
    key="emergency_severity"
)

issue = st.text_input("Emergency Description")

if st.button("🚨 RECORD EMERGENCY"):
    if not patient or not issue:
        st.warning("Please enter the patient ID and emergency description.")
    else:
        try:
            response = requests.post(
                f"{BACKEND_URL}/api/emergency-triage/",
                json={
                    "patient": patient,
                    "severity": severity,
                    "issue": issue
                },
                timeout=5
            )

            if response.status_code == 200:
                st.success("🟢 Emergency case recorded!")
                st.json(response.json())
            else:
                st.error(f"🔴 Failed: {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"🔴 Backend connection failed: {e}")

# =========================================================
# COMMUNICATIONS
# =========================================================

elif page == "📡 Communications":

    st.subheader("📡 Communications")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Network Health",
            "45%",
            "-12%"
        )

    with col2:

        st.metric(
            "Signal Strength",
            "32%",
            "-18%"
        )

    with col3:

        st.metric(
            "Latency",
            "840 ms",
            "+210 ms"
        )


    st.divider()


    st.markdown("""
    <div class="card">

    <h3>📡 Communication Status</h3>

    <p>
    🔴 Primary communication channel: DISRUPTED
    </p>

    <p>
    🟡 Backup channel: DEGRADED
    </p>

    <p>
    🟢 ROVER-01 relay capability: AVAILABLE
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.subheader("🛠️ Recovery Plan")

    recovery = pd.DataFrame({

        "Step": [
            1,
            2,
            3,
            4
        ],

        "Action": [
            "Deploy relay rover",
            "Establish temporary node",
            "Restore colony network",
            "Reconnect ASTRA-1"
        ],

        "Status": [
            "READY",
            "PENDING",
            "PENDING",
            "PENDING"
        ]

    })

    st.dataframe(
        recovery,
        use_container_width=True,
        hide_index=True
    )

st.subheader("📡 Communication Recovery")

channel = st.selectbox(
    "Select Communication Channel",
    [
        "RELAY-01",
        "ORBITAL-SAT",
        "ROVER-RELAY",
        "EMERGENCY-BAND"
    ],
    key="communication_channel"
)

action = st.selectbox(
    "Recovery Action",
    [
        "DEPLOY RELAY",
        "RESTORE PRIMARY LINK",
        "SWITCH TO EMERGENCY BAND",
        "BOOST SIGNAL"
    ],
    key="communication_action"
)

if st.button("📡 EXECUTE RECOVERY"):
    try:
        response = requests.post(
            f"{BACKEND_URL}/api/communication-action/",
            json={
                "channel": channel,
                "action": action
            },
            timeout=5
        )

        if response.status_code == 200:
            st.success("🟢 Communication recovery action recorded!")
            st.json(response.json())
        else:
            st.error(f"🔴 Failed: {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"🔴 Backend connection failed: {e}")

# =========================================================
# MISSION RECOMMENDATION
# =========================================================

elif page == "🧠 Mission Recommendation":

    st.subheader("🧠 Mission Recommendation")


    st.markdown("""
    <div class="card">

    <h2>🧠 Decision Pipeline</h2>

    <p>📊 Collect telemetry</p>

    <p>🔍 Analyze system conditions</p>

    <p>⚠️ Identify critical threats</p>

    <p>🎯 Prioritize actions</p>

    <p>🤖 Deploy autonomous systems</p>

    <p>🔄 Monitor and adapt</p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="card">

    <h2>🚨 RECOMMENDED ACTION</h2>

    <p>
    Prioritize communication recovery and deploy
    ROVER-01 as a relay-capable unit while continuing
    the ASTRA-1 search.
    </p>

    </div>
    """, unsafe_allow_html=True)


    if st.button("✅ EXECUTE RECOMMENDATION"):

        st.success(
            "Mission action queued successfully."
        )


    st.divider()


    st.subheader("📋 Action Priority")

    priority_data = pd.DataFrame({

        "Priority": [
            "01",
            "02",
            "03",
            "04"
        ],

        "Action": [
            "Restore communications",
            "Deploy ROVER-01",
            "Locate ASTRA-1",
            "Stabilize oxygen production"
        ],

        "Status": [
            "IMMEDIATE",
            "READY",
            "ACTIVE",
            "CRITICAL"
        ]

    })

    st.dataframe(
        priority_data,
        use_container_width=True,
        hide_index=True
    )

st.markdown("### 🧠 AI-Assisted Mission Assessment")

try:
    response = requests.get(
        f"{BACKEND_URL}/api/status/",
        timeout=5
    )

    if response.status_code == 200:
        mission_data = response.json()

        status = mission_data.get("status", "UNKNOWN")
        oxygen = mission_data.get("oxygen", "UNKNOWN")
        communication = mission_data.get("communication", "UNKNOWN")
        astra_signal = mission_data.get("astra_signal", "UNKNOWN")

        st.info(
            f"""
            **Current Mission State**

            🚨 Mission Status: **{status}**

            🫁 Oxygen: **{oxygen}**

            📡 Communication: **{communication}**

            🪐 Astra Signal: **{astra_signal}**
            """
        )

        if communication == "DISRUPTED":
            recommendation = (
                "Prioritize communication recovery while "
                "continuing the Astra search."
            )
        elif astra_signal == "DETECTED":
            recommendation = (
                "Maintain Astra search operations and "
                "coordinate the nearest available rover."
            )
        else:
            recommendation = (
                "Continue monitoring mission telemetry "
                "and reassess the situation."
            )

        st.success("🧠 Recommended Mission Action")

        st.write(f"### ➜ {recommendation}")

        st.caption(
            "Recommendation generated from prototype mission data."
        )

    else:
        st.error("Unable to retrieve mission data.")

except requests.exceptions.RequestException:
    st.error("Backend connection unavailable.")

# =========================================================
# FOOTER
# =========================================================

current_time = datetime.now().strftime("%H:%M:%S")

st.markdown(
    f"""
    <div class="footer">

    🚀 ASTRA-1 MISSION CONTROL
    • SYSTEM TIME: {current_time}
    • SIMULATION MODE
    • ALL SYSTEMS MONITORED

    </div>
    """,
    unsafe_allow_html=True
)