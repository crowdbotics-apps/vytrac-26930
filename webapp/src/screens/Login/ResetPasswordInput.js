import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import '../../App.css';

import {store} from '../../util/store'

import passwordLogo from '../../assets/images/password.png';

class LoginForm extends Component {

  constructor(props) {
    store.init();
    super(props);
    this.state = {}
  }

  validate () {
    if (!this.state.password1) {
      alert("Please fill your username");
      return false;
    } else if (!this.state.password2) {
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

  gotNumber(fieldIndex) {
    const nextSibling = document.querySelector(
      `input[name=number${fieldIndex + 1}]`
    );
    // If found, focus the next field
    if (nextSibling !== null) {
      nextSibling.focus();
    }
  }

  render() {
    return (
        <div> 
            <Row className="vertical-container">
                <Col className="line-container">
                  <div className="grey-line-inv"></div>
                </Col>
                <Col className="line-container">
                  <div className="green-line-inv"></div>
                </Col>
              </Row>  

              <div className="centered-logo">
                <div className="logo-container">
                  <img className="shield-logo" src={passwordLogo}></img>
                </div>
              </div>

              <p className="text-left normal-text" style={{marginTop: 30}}>Reset my password</p>

              <p className="text-left smaller-text">Set your new password</p>

              <p className="grey-text password-label top25">Password</p>
              <input onChange={(username) => this.setState({password1: username})} className="text-field" type="password" name="password1" />
              <p className="grey-text password-label" style={{fontSize: 8, marginTop: 5}}>It must be 8 characters or more, have at least 1 number, 1 special character and 1 upper case</p>

              <p className="grey-text password-label top15">Confirm password</p>
              <input onChange={(username) => this.setState({password2: username})} className="text-field" type="password" name="password2" />

              <div className="token-bottom-buttons-container-smaller">
                <Button onClick={() => this.props.changeItem('login')}  style={{marginRight: '55%'}}  variant="light">CANCEL</Button>
                <Button onClick={() => this.login()}>CONTINUE</Button>
              </div>
        </div>
    );
  }
}

export default LoginForm;