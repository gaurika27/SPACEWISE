function openResearcherPage() {
  window.location.href = "researcher.html";
}

function openEnthusiastPage() {
  window.location.href = "enthusiast.html";
}

function openLoginPage() {
  window.location.href = "login.html";
}
function openRegisterPage() {
  window.location.href = "register.html";
}
function openhepPage() {
  window.location.href = "helpcentre.html";
}
function openFeedbackPage() {
  window.location.href = "feedback.html";
}
function openChatbotPage() {
  window.location.href = "chatbot.html";
}
function openAboutusPage() {
  window.location.href = "aboutus.html";
}

function openCommunityPage() {
  window.location.href = "community.html";
}

function openEducationPage() {
  window.location.href = "education.html";
}
function openAsteroidtrackingPage() {
  window.location.href = "asteroidtracker.html";
}
function openSatelliteTrackingPage() {
  window.location.href = "https://satellitemap.space/";
}
const loadModel = async () => {
  const model = await mobilenet.load();
  console.log("Model loaded successfully");
  return model;
};
