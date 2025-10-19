const calendarEl = document.getElementById('calendar');
    const monthYear = document.getElementById('monthYear');
    const prevBtn = document.getElementById('prevMonth');
    const nextBtn = document.getElementById('nextMonth');
    const eventModal = new bootstrap.Modal(document.getElementById('eventModal'));
    const modalDate = document.getElementById('modalDate');
    const eventList = document.getElementById('eventList');
    const addEventForm = document.getElementById('addEventForm');
    const eventTitle = document.getElementById('eventTitle');
    const eventTime = document.getElementById('eventTime');

    let currentDate = new Date();
    let selectedDate = null;

    const STORAGE_KEY = 'agenda_simple_calendar';

    function getEvents() {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
    }

    function saveEvents(events) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(events));
    }

    function renderCalendar() {
      calendarEl.querySelectorAll('.day').forEach(d => d.remove());

      const year = currentDate.getFullYear();
      const month = currentDate.getMonth();

      const firstDay = new Date(year, month, 1);
      const lastDay = new Date(year, month + 1, 0);
      const startDay = firstDay.getDay();

      const prevMonthLast = new Date(year, month, 0).getDate();

      monthYear.textContent = currentDate.toLocaleDateString('pt-BR', { month: 'long', year: 'numeric' });

      const days = [];

      // Dias do mês anterior
      for (let i = startDay - 1; i >= 0; i--) {
        days.push({ day: prevMonthLast - i, other: true, date: new Date(year, month - 1, prevMonthLast - i) });
      }

      // Dias do mês atual
      for (let i = 1; i <= lastDay.getDate(); i++) {
        days.push({ day: i, other: false, date: new Date(year, month, i) });
      }

      // Preenche com dias do próximo mês
      while (days.length % 7 !== 0) {
        const nextDate = new Date(year, month, lastDay.getDate() + (days.length % 7));
        days.push({ day: nextDate.getDate(), other: true, date: nextDate });
      }

      const events = getEvents();

      days.forEach(({ day, other, date }) => {
        const div = document.createElement('div');
        div.className = 'day position-relative';
        if (other) div.classList.add('other-month');
        if (isSameDate(date, new Date())) div.classList.add('today');

        const dateStr = formatDate(date);
        div.innerHTML = `<div>${day}</div>`;

        const evList = events[dateStr] || [];
        evList.slice(0,2).forEach(e => {
          const pill = document.createElement('div');
          pill.className = 'event-pill';
          pill.textContent = (e.time ? e.time + ' ' : '') + e.title;
          div.appendChild(pill);
        });

        div.addEventListener('click', () => openModal(date));
        calendarEl.appendChild(div);
      });
    }

    function isSameDate(a, b) {
      return a.getFullYear() === b.getFullYear() && a.getMonth() === b.getMonth() && a.getDate() === b.getDate();
    }

    function formatDate(date) {
      return date.toISOString().split('T')[0];
    }

    function openModal(date) {
      selectedDate = date;
      modalDate.textContent = formatDate(date);
      renderEventList();
      eventModal.show();
    }

    function renderEventList() {
      const events = getEvents();
      const dateStr = formatDate(selectedDate);
      const evList = events[dateStr] || [];
      eventList.innerHTML = '';

      if (evList.length === 0) {
        eventList.innerHTML = '<p class="text-muted">Nenhum evento para este dia.</p>';
        return;
      }

      evList.forEach((ev, i) => {
        const item = document.createElement('div');
        item.className = 'd-flex justify-content-between align-items-center border rounded p-2 mb-2';
        item.innerHTML = `<div><strong>${ev.title}</strong><br><small>${ev.time || ''}</small></div><button class='btn btn-sm btn-outline-danger'>Excluir</button>`;
        item.querySelector('button').addEventListener('click', () => {
          evList.splice(i, 1);
          events[dateStr] = evList;
          saveEvents(events);
          renderEventList();
          renderCalendar();
        });
        eventList.appendChild(item);
      });
    }

    addEventForm.addEventListener('submit', e => {
      e.preventDefault();
      const title = eventTitle.value.trim();
      if (!title) return;
      const events = getEvents();
      const dateStr = formatDate(selectedDate);
      events[dateStr] = events[dateStr] || [];
      events[dateStr].push({ title, time: eventTime.value });
      saveEvents(events);
      eventTitle.value = '';
      eventTime.value = '';
      renderEventList();
      renderCalendar();
    });

    prevBtn.addEventListener('click', () => { currentDate.setMonth(currentDate.getMonth() - 1); renderCalendar(); });
    nextBtn.addEventListener('click', () => { currentDate.setMonth(currentDate.getMonth() + 1); renderCalendar(); });

    renderCalendar();