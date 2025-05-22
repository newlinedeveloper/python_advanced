🎯 Goal: Build a basic React interface to:

* List all vehicles
* Add a new vehicle
* (Optionally) view/add components

🧱 React Frontend Setup (Step-by-Step)

Step 1: Create the React App

In your root project directory (sibling to the Django backend):

```bash
npx create-react-app vehicle-ui
cd vehicle-ui
npm install axios react-router-dom
```

(Optional: Rename the default App.js to App.jsx if you prefer JSX naming convention.)

Step 2: Set Up Axios for API Calls

Create a file: src/api.js

```js
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

export default API;
```

Step 3: Create Vehicle List Component

Create src/components/VehicleList.jsx:

```jsx
import React, { useEffect, useState } from 'react';
import API from '../api';

function VehicleList() {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    API.get('vehicles/')
      .then(res => setVehicles(res.data))
      .catch(err => console.error('Error fetching vehicles:', err));
  }, []);

  return (
    <div>
      <h2>Vehicle List</h2>
      <ul>
        {vehicles.map(v => (
          <li key={v.id}>
            {v.name} ({v.model_year}) - {v.variant}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default VehicleList;
```

Step 4: Create Vehicle Form to Add Vehicles

Create src/components/AddVehicleForm.jsx:

```jsx
import React, { useState } from 'react';
import API from '../api';

function AddVehicleForm() {
  const [form, setForm] = useState({
    name: '',
    model_year: '',
    variant: ''
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    API.post('vehicles/', form)
      .then(() => {
        alert('Vehicle added!');
        setForm({ name: '', model_year: '', variant: '' });
      })
      .catch(err => console.error('Failed to add vehicle', err));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Add Vehicle</h3>
      <input name="name" placeholder="Vehicle Name" value={form.name} onChange={handleChange} required />
      <input name="model_year" placeholder="Model Year" value={form.model_year} onChange={handleChange} required />
      <input name="variant" placeholder="Variant" value={form.variant} onChange={handleChange} required />
      <button type="submit">Add</button>
    </form>
  );
}

export default AddVehicleForm;
```

Step 5: Wire It All in App.jsx

Replace src/App.js with:

```jsx
import React from 'react';
import VehicleList from './components/VehicleList';
import AddVehicleForm from './components/AddVehicleForm';

function App() {
  return (
    <div className="App">
      <h1>Vehicle Configuration Platform</h1>
      <AddVehicleForm />
      <VehicleList />
    </div>
  );
}

export default App;
```

Step 6: Enable CORS in Django

Install Django CORS Headers:

```bash
pip install django-cors-headers
```

In settings.py:

Add to INSTALLED\_APPS:

```python
'corsheaders',
```

Add middleware (above CommonMiddleware):

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
```

Allow localhost (for development):

```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
```

Step 7: Run Both Servers

Start Django backend:

```bash
python manage.py runserver
```

Start React frontend:

```bash
cd vehicle-ui
npm start
```

Now open [http://localhost:3000](http://localhost:3000) — you should see your React app connected to the Django backend!

✅ What’s Next?

* Add component form and list?
* Connect simulation start/status?
* Add navigation with React Router?

Let me know what you'd like to build next!
