async function loadDashboard() {
    const data = await fetchData("/dashboard");

    document.getElementById("stats").innerHTML = `
        <h3>Total EC2: ${data.EC2}</h3>
        <h3>S3 Buckets: ${data.S3}</h3>
        <h3>VPCs: ${data.VPC}</h3>
        <h3>Security Groups: ${data.SecurityGroups}</h3>
        <h3>Volumes: ${data.Volumes}</h3>
        <h3>Snapshots: ${data.Snapshots}</h3>
        <h3>Elastic IPs: ${data.ElasticIPs}</h3>
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
