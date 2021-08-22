import React from 'react';
import 'leaflet/dist/leaflet.css';
import 'normalize.css/normalize.css';
import '@blueprintjs/core/lib/css/blueprint.css';
import '@blueprintjs/icons/lib/css/blueprint-icons.css';

// Custom pages
import NavBar from './components/navbar';
import HomePage from './pages/home';


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      location: [-35, 117]
    }
  }

  globalStateHandler = (newstate) => {
    this.setState(newstate);
  }

  render() {
    return (
      <div>

        <HomePage state={this.state} globalStateHandler={this.globalStateHandler} />
      </div>
    );
  }
}


export default App;
