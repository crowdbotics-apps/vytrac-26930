import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import '../../App.css';

import {store} from '../../util/store'

import passwordLogo from '../../assets/images/password.png';

class ResetPassword extends Component {

  constructor(props) {
    store.init();
    super(props);
    this.state = {}
  }

  validate () {
    if (!this.state.username) {
      alert("Please fill your email");
      return false;
    } else {
      return true;
    }
  }

  login() { 
    if(this.validate()) {
      try {
        this.props.changeItem('reset-password-input');
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
        <div style={{height: '100%'}}> 
            <Row className="vertical-container">
                <Col style={{padding: 0, margin: 0}}>
                  <div className="green-line"></div>
                </Col>
                <Col style={{padding: 0, margin: 0}}>
                  <div className="grey-line"></div>
                </Col>
              </Row>  

              <div className="centered-logo">
                <div className="logo-container">
                  <img className="shield-logo" src={passwordLogo}></img>
                </div>
              </div>

              <p className="text-left normal-text top25" style={{marginTop: 30}}>Forgot my password</p>

              <p className="text-left smaller-text">Enter the email you used to register your Vytrac account.</p>

              <p className="grey-text password-label top25">Email</p>
              <input onChange={(username) => this.setState({username: username})} className="text-field" type="input" name="password" />

              <div className="token-bottom-buttons-container">
                <Button onClick={() => this.props.changeItem('login')}  style={{marginRight: '55%'}} variant="light">CANCEL</Button>
                <Button onClick={() => this.login()}>NEXT</Button>
              </div>
        </div>
    );
  }
}

export default ResetPassword;