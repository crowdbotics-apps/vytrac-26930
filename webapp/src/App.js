import React, { Component, View } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  withRouter
} from "react-router-dom";

import './App.css';

import {store} from './util/store'

import Login from './screens/Login/Login'
import ProviderDashboard from './screens/ProviderDashboard/ProviderDashboard'

class App extends Component {

  constructor(props) {
    store.init();
    super(props);
    this.state = {}
  }

  validate () {
    if (!this.state.username) {
      alert("Please fill your username");
      return false;
    } else if (!this.state.password) {
      alert("Please fill your password");
      return false;
    } else {
      return true;
    }
  }

  login() { 
    if(this.validate()) {
      try {
        store.data.login(this.state.username + '', this.state.password + '').then((result) => {
          if(result) {
            alert("Successful login!");
          } else {
            alert("Could not login");
          }
        });
      } catch (ex) {
        alert("Could not login");
      }
    }
  }

  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route path="/login">
              <Login />
            </Route>
            <Route path="/dashboard">
              <ProviderDashboard />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default withRouter(App);