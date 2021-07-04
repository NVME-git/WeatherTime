import React, { useState } from 'react';
const api = require('./config.json')

function App() {
  const [query, setQuery] = useState('');
  const [weather, setWeather] = useState({});
  const [units, setUnits] = useState({temp_type:'Metric', temp_symbol: '°C'});
  const [endpoint, setEndpoint] = useState({name:"capital", param:"Country"});
  const [buttons, setButtons] = useState({capital:'white', city:'rgba(255, 255, 255, 0.85)'});

  const switchEndpoint = evt => {
    if (evt === 'capital') {
      setEndpoint({name:"capital", param:"Country"})
      setButtons({capital:'white', city:'rgba(255, 255, 255, 0.85)'})
    }
    if (evt === 'city') {
      setEndpoint({name:"city", param:"City"})
      setButtons({city:'white', capital:'rgba(255, 255, 255, 0.85)'})
    }
    // console.log(buttons)
  }

  const search = (query) => {
    let d = new Date();
    let user_tz = -1*d.getTimezoneOffset();
    console.log(query, user_tz, 'metric');
    let uri = `${api.backup.base}/${endpoint.name}weather?${endpoint.param}=${query}&UserTimeZone=${user_tz}&Units=metric`;
    let request_headers= new Headers();
    request_headers.append('Content-Type','application/json');
    request_headers.append('Accept','application/json');
    request_headers.append('x-api-key',api.backup.key);
    request_headers.append('Host','http//192.168.91.241:3000');
    let request = new Request(uri, {
      method: 'GET',
      mode: 'cors',
      headers: request_headers})
    fetch(request)
      .then(res => res.json())
      .then(result => {
        setWeather(result);
        setQuery('');
        console.log(result);})
      .catch(error => console.log(error));
  }

  const key_search = evt => {
    if (evt.key === "Enter") search(query)
  }

  const switchUnits = () => {
    if (units.temp_type === 'Metric') {
      setUnits({temp_type:'Imperial', temp_symbol: '°F'})
    }
    else if (units.temp_type === 'Imperial') {
      setUnits({temp_type:'Standard', temp_symbol: 'K'})
    }
    else if (units.temp_type === 'Standard') {
      setUnits({temp_type:'Metric', temp_symbol: '°C'})
    }
  }

  const unitsBuilder = (temperature) => {
    // console.log(units)
    if (units.temp_type === 'Metric') return Math.round(temperature);
    if (units.temp_type === 'Imperial') return Math.round((temperature*9/5)+32);
    if (units.temp_type === 'Standard') return Math.round(temperature+273);
  }

  const timeZoneBuilder = (n) => {
    if (n === 0) return "Same Time";
    let hours = "hours";
    if (Math.abs(n) === 1) hours = "hour";
    let ahead = "behind";
    if (n < 0) {
      n = -1*n;
      ahead = "ahead";
    }
    return `${n} ${hours} \n ${ahead}`
  }

  const dateBuilder = (d) => {
    let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    let day = days[d.getDay()];
    let date = d.getDate();
    let month = months[d.getMonth()];
    let year = d.getFullYear();

    return `${day} ${date} ${month} ${year}`
  }

  return (
    <div className={(typeof weather.City != "undefined") ? ((weather.Temperature > 20) ? 'app warm' : 'app') : 'app'}>
      <main>
        <div className="search-box">
          <div className='api' tabIndex="1" 
            style={{backGroundColor:buttons.capital}}
            onClick={() => switchEndpoint('capital')}>
            Capital
          </div>
          <div className='api' tabIndex="2" 
            style={{backGroundColor:buttons.city}}
            onClick={() => switchEndpoint('city')}>
            City
          </div>
          <input 
            type="text"
            className="search-bar"
            placeholder={`${endpoint.param} search`}
            onChange={e => setQuery(e.target.value)}
            value={query}
            onKeyPress={key_search}
          />
        </div>
        {(typeof weather.City != "undefined") ? (
        <div>
          <div className="location-box">
            <div className="location">{weather.City}, {weather.CountryCode}</div>
            <div className="date">{dateBuilder(new Date())}</div>
          </div>
          <div className="weather-box"
            onClick={switchUnits}
          >
            <div className="temp">
              {unitsBuilder(weather.Temperature)}{units.temp_symbol}
            </div>
          </div>
          <div className="time-difference">{timeZoneBuilder(weather.TimeDifference)}</div>
        </div>
        ) : ('')}
      </main>
    </div>
  );
}

export default App;