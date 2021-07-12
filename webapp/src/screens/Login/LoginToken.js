import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import '../../App.css';

import {store} from '../../util/store'

import shieldLogo from '../../assets/images/secure-shield.png';

class LoginForm extends Component {

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
                <Col style={{padding: 0, margin: 0}}>
                  <div className="grey-line-inv"></div>
                </Col>
                <Col style={{padding: 0, margin: 0}}>
                  <div className="green-line-inv"></div>
                </Col>
              </Row>  

              <div className="centered-logo">
                <div className="logo-container">
                  <img className="shield-logo" src={shieldLogo}></img>
                </div>
              </div>

              <p className="text-left normal-text top25" style={{marginTop: 30}}>Security token</p>

              <p className="text-left smaller-text">Enter your 6 digit verification code sent to <b>user@email.com</b>. Didn’t receive your code yet? <a href="#">Send it again.</a></p>

              <div className="vertical-container centered top25">
                <input autocomplete="off" onChange={(item) => {this.gotNumber(1); this.setState({number1: item})}} className="text-field-token" style={{marginLeft: 0}} type="text" name="number1" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(2); this.setState({number2: item})}} className="text-field-token" type="text" name="number2" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(3); this.setState({number3: item})}} className="text-field-token" type="text" name="number3" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(4); this.setState({number4: item})}} className="text-field-token" type="text" name="number4" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(5); this.setState({number5: item})}} className="text-field-token" type="text" name="number5" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(6); this.setState({number6: item})}} className="text-field-token" style={{marginRight: 0}} type="text" name="number6" />
              </div>

              <div className="token-bottom-buttons-container">
                <Button onClick={() => this.props.changeItem('login')} style={{marginRight: 95}} variant="light">CANCEL</Button>
                <Button onClick={() => this.login()}>CONTINUE</Button>
              </div>
        </div>
    );
  }
}

export default LoginForm;