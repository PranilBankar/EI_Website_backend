fetch('/api/members/')
  .then(res => res.json())
  .then(data => {
      let html = '<ul>';
      data.forEach(member => {
          html += `<li>${member.name} - ${member.role}</li>`;
      });
      html += '</ul>';
      document.getElementById('members').innerHTML = html;
  });
