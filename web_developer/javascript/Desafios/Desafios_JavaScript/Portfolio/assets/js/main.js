// Recebe os dados do perfil e insere no corpo do site
(async function createPortfolio() {
    const profileData = await fetchProfile();
    const profileHTML = jsonToHTML(profileData);
    const main = document.querySelector('.main');
    main.innerHTML = profileHTML.join('');
    addClickEvent();
})()

// Cria a estrutura HTML do site através de um json
function jsonToHTML(json) {
    const HTML = [`<header class="header">
            <a href="${json.url}" target="_blank" rel="external"><img class="photo" src="${json.photo}" alt="Minha foto de perfil"></a>
            <h1 class="title">Olá, me chamo ${json.name}</h1>
            <div class="information">
                <p class="location">${json.location}</p>
                <p class="phone"><a href="tel:${json.phone}">${json.phone}</a></p>
                <p class="email"><a href="mailto:${json.email}">${json.email}</a></p>
            </div>
        </header>`,
        `<section class="acordeon">
            <button class="trigger" type="button"><h2 class="acordeon-title">Skills</h2></button>
            <div class="content">
                <div class="skills-container">
                    <h3>Habilidades profissionais:</h3>
                    <ul class="work-skills">
                        ${json.skills.hardSkills.map((skill) => {
                            return `<li><img src="assets/img/svg/${skill.name.toLowerCase()}.svg" alt="${skill.name}" title="${skill.name}"</li>`;
                        }).join('')}
                    </ul>
                </div>
                <div class="skills-container">
                    <h3>Habilidades pessoais:</h3>
                    <ul class="personal-skills">
                        ${json.skills.softSkills.map((skill) => `<li>${skill}</li>`).join('')}
                    </ul>
                </div>
            </div>
        </section>`,
        `<section class="acordeon">
            <button class="trigger" type="button"><h2 class="acordeon-title">Idiomas</h2></button>
            <div class="content">
                <ul class="languages">
                    ${json.languages.map((language) => `<li>${language}</li>`).join('')}
                </ul>
            </div>
        </section>`,
        `<section class="acordeon">
            <button class="trigger" type="button"><h2 class="acordeon-title">Educação</h2></button>
            <div class="content">
                <ul class="education">
                    ${json.education.colleges.map((college) => {
                        return `<li><span class="${college.name.toLowerCase()} college">${college.name}</span> - ${college.course} - ${college.date}</li>`
                    })}
                </ul>
                <h3>Cursos</h3>
                <ul class="education">
                    ${json.education.courses.map((course) => {
                        return `<li class="course"><span class="${course.name.toLowerCase().replace(' ', '-')}">${course.name}</span> - ${course.workload} - <span class="institution">${course.institution}</span> </li>`
                    }).join('')}
                </ul>
            </div>
        </section>`,
        `<section class="acordeon">
            <button class="trigger" type="button"><h2 class="acordeon-title">Portfólio</h2></button>
            <div class="content">
                <ul class="portfolio">
                    ${json.portfolio.map((project) => {
                        return `<li>
                            <h3 class="${project.github? 'github': ''}">${project.name}</h3>
                            <a href="${project.url}" target="_blank">${project.url}</a>
                        </li>`
                    }).join('')}
                </ul>
            </div>
        </section>`]
        return HTML;
}
