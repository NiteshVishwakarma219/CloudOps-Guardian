async function loadDashboard() {
    const data = await fetchData("/dashboard");

    document.getElementById("stats").innerHTML = `
        <h3>Total EC2: ${data.ec2_total}</h3>
        <h3>Running: ${data.ec2_running}</h3>
        <h3>Stopped: ${data.ec2_stopped}</h3>
        <h3>S3 Buckets: ${data.s3_total}</h3>
        <h3>Estimated Savings: $${data.savings}</h3>
    `;
}

loadDashboard();
function toggleDarkMode() {
    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {
        localStorage.setItem("theme", "dark");
        showToast("Dark mode enabled");
    } else {
        localStorage.setItem("theme", "light");
        showToast("Light mode enabled");
    }
}

window.onload = () => {
    const theme = localStorage.getItem("theme");

    if (theme === "dark") {
        document.body.classList.add("dark");
    }
    
};
async function loadDashboard() {
    const data = await fetchData("/dashboard");

    console.log(data);   // Add this line

    document.getElementById("stats").innerHTML = `
        <h3>Total EC2: ${data.ec2_total}</h3>
        <h3>Running: ${data.ec2_running}</h3>
        <h3>Stopped: ${data.ec2_stopped}</h3>
        <h3>S3 Buckets: ${data.s3_total}</h3>
        <h3>Estimated Savings: $${data.savings}</h3>
    `;
}

loadDashboard();