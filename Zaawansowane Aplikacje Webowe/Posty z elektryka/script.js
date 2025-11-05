async function loadPosts() {
  const blogUrl = 'https://zsegw.pl/blog';
  const proxyUrl = 'https://api.allorigins.win/get?url=' + encodeURIComponent(blogUrl);

  try {
    const response = await fetch(proxyUrl);
    const data = await response.json();
    const html = data.contents;

    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');

    const articles = Array.from(doc.querySelectorAll('article')).slice(0, 3);

    if (articles.length === 0) {
      document.getElementById('post1').textContent = 'Nie znaleziono postów.';
      return;
    }

    articles.forEach((article, i) => {
      const link = article.querySelector('a')?.href || '#';
      const title = (article.querySelector('h2, h3, .entry-title')?.textContent || 'Bez tytułu')
                    .replace(/Post last modified:.*/i, '').trim();
      const img = article.querySelector('img')?.src || 'https://via.placeholder.com/120?text=Brak+obrazka';
      const excerpt = (article.querySelector('p')?.textContent || '')
                    .replace(/Post last modified:.*/i, '').trim();

      const postDiv = document.getElementById(`post${i+1}`);
      postDiv.innerHTML = `
        <img src="${img}" class="thumb" alt="Miniaturka">
        <div class="content">
          <div class="title">${title}</div>
          <div class="excerpt">${excerpt}</div>
        </div>
      `;
      postDiv.onclick = () => window.open(link, '_blank');
    });
  } catch (err) {
    console.error(err);
    document.getElementById('post1').textContent = 'Błąd ładowania postów.';
  }
}

loadPosts();