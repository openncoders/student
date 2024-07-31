document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  const searchButton = document.getElementById('searchButton');
  const suggestionsList = document.getElementById('suggestionsList');
  const teachersList = document.getElementById('teachersList');

  const fetchSuggestions = () => {
    const query = searchInput.value;

    if (query.length < 3) {
      suggestionsList.innerHTML = '';  // Clear suggestions if the query is too short
      return;
    }

    fetch(`/search/?q=${query}`)
      .then(response => response.json())
      .then(data => {
        console.log('Suggestions data:', data);  // Log the data for debugging
        suggestionsList.innerHTML = '';

        data.forEach(teacher => {
          const li = document.createElement('li');
          li.textContent = `${teacher.name} ${teacher.surname}`;
          li.className = 'suggestions-list-item';
          li.addEventListener('click', () => {
            searchInput.value = `${teacher.name} ${teacher.surname}`;
            suggestionsList.innerHTML = '';
            handleSearch();  // Trigger the search when a suggestion is clicked
          });
          suggestionsList.appendChild(li);
        });
      })
      .catch(error => console.error('Error fetching suggestions:', error));
  };

  const handleSearch = () => {
    const query = searchInput.value;

    if (query.length < 3) {
      // Do nothing if the query is too short
      return;
    }

    fetch(`/search/?q=${query}`)
      .then(response => response.json())
      .then(data => {
        console.log('Search results data:', data);  // Log the data for debugging
        teachersList.innerHTML = '';  // Clear the current list of teachers

        if (data.length === 0) {
          const noResults = document.createElement('li');
          noResults.textContent = 'No results found';
          noResults.className = 'teachers__list-item';
          teachersList.appendChild(noResults);
          return;
        }

        data.forEach(teacher => {
          const li = document.createElement('li');
          li.className = 'teachers__list-item';
          li.innerHTML = `
            <div class="onHover">Подробнее</div>
            <div class="teachers__list-item__img">
              <img src="{% static 'images/123.png' %}" alt="My image">
              <div class="teachers__list-item__img-mark">
                <span>4.8</span>
                <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
                  xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                  viewBox="0 0 426.667 426.667" style="enable-background: new 0 0 426.667 426.667"
                  xml:space="preserve">
                  <polygon style="fill: #fac917"
                    points="213.333,10.441 279.249,144.017 426.667,165.436 320,269.41 345.173,416.226 213.333,346.91
                      81.485,416.226 106.667,269.41 0,165.436 147.409,144.017 " />
                </svg>
              </div>
            </div>
            <div class="teachers__list-item__info">
              <div>
                <div class="teachers__list-item__info-name">${teacher.name} ${teacher.surname}</div>
                <div class="teachers__list-item__info-uni">
                  Самарский государственный технический университет
                </div>
              </div>
              <div class="teachers__list-item__info-less">
                ${teacher.characteristic}
              </div>
            </div>
          `;
          teachersList.appendChild(li);
        });
      })
      .catch(error => console.error('Error fetching search results:', error));
  };

  searchInput.addEventListener('input', fetchSuggestions);
  searchButton.addEventListener('click', handleSearch);
});
