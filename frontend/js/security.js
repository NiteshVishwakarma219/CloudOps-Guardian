async function loadSecurity() {
    const data = await fetchData("/security");

    // Security Score Cards
    document.getElementById("securityCards").innerHTML = `
        <div class="card">
            <h3>Public S3 Buckets</h3>
            <p>${data.public_s3}</p>
        </div>

        <div class="card">
            <h3>Open Security Groups</h3>
            <p>${data.open_sg}</p>
        </div>

        <div class="card">
            <h3>IAM Without MFA</h3>
            <p>${data.iam_no_mfa}</p>
        </div>

        <div class="card">
            <h3>Unencrypted EBS</h3>
            <p>${data.unencrypted_ebs}</p>
        </div>

        <div class="card">
            <h3>Root Usage</h3>
            <p>${data.root_usage}</p>
        </div>

        <div class="card">
            <h3>Security Score</h3>
            <p>${data.security_score}/100</p>
        </div>
    `;

    // Risky resources list
    let risksHTML = "";

    data.risks.forEach(item => {
        risksHTML += `
            <div class="card" style="border-left: 5px solid red;">
                <h4>${item.type}</h4>
                <p>${item.name}</p>
            </div>
        `;
    });

    document.getElementById("riskList").innerHTML = risksHTML;
}

loadSecurity();