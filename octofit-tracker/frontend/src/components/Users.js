import React, { useEffect, useState } from 'react';

const Users = () => {
  const [data, setData] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched users:', results);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, [endpoint]);

  return (
    <div>
      <h1 className="mb-4 display-6">Users</h1>
      <div className="card">
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-striped table-hover">
              <thead>
                <tr>
                  {data[0] && Object.keys(data[0]).map((key) => (
                    <th key={key}>{key}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {data.map((item, idx) => (
                  <tr key={item.id || idx}>
                    {data[0] && Object.keys(data[0]).map((key) => (
                      <td key={key}>{String(item[key])}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
            {data.length === 0 && <div className="text-muted">Geen gebruikers gevonden.</div>}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Users;
