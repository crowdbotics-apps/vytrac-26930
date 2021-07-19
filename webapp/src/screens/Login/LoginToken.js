import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { withRouter } from "react-router-dom";

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
    if (!this.state.number1 && !this.state.number2 && !this.state.number3 && !this.state.number4 && !this.state.number5 && !this.state.number6) {
      alert("Please fill all the numbers from your token");
      return false;
    } else {
      return true;
    }
  }

  login() { 
    if(this.validate()) {
      try {
        console.log(this.props.history);
        this.props.history.push('/dashboard');
      } catch (ex) {
        console.log(this.state);
        alert("Could not login");
      }
    } else {
      return false;
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
                  <img className="shield-logo" resizeMode={'stretch'} src={shieldLogo}></img>
                </div>
              </div>

              <p className="text-left normal-text top25 dynamic-font-heading" style={{marginTop: 30}}>Security token</p>

              <p className="text-left smaller-text dynamic-font-normal">Enter your 6 digit verification code sent to <b>user@email.com</b>. Didn’t receive your code yet? <a href="#">Send it again.</a></p>

              <div className="vertical-container centered top25">
                <input autocomplete="off" onChange={(item) => {this.gotNumber(1); this.setState({number1: item.target.value})}} className="text-field-token dynamic-font-huge" style={{marginLeft: 0}} type="text" name="number1" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(2); this.setState({number2: item.target.value})}} className="text-field-token dynamic-font-huge" type="text" name="number2" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(3); this.setState({number3: item.target.value})}} className="text-field-token dynamic-font-huge" type="text" name="number3" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(4); this.setState({number4: item.target.value})}} className="text-field-token dynamic-font-huge" type="text" name="number4" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(5); this.setState({number5: item.target.value})}} className="text-field-token dynamic-font-huge" type="text" name="number5" />
                <input autocomplete="off" onChange={(item) => {this.gotNumber(6); this.setState({number6: item.target.value})}} className="text-field-token dynamic-font-huge" style={{marginRight: 0}} type="text" name="number6" />
              </div>

              <Row className="bottom-button-container">
                <Col xs={2}>
                  <Button onClick={() => this.props.changeItem('login')}  className="dynamic-font-normal text-bold" style={{marginRight: '55%'}} variant="light">CANCEL</Button>
                </Col>
                <Col xs={8}>
                </Col>
                <Col xs={2}>
                  <Button disabled={!this.state.number1 || !this.state.number2 || !this.state.number3 || !this.state.number4 || !this.state.number5 || !this.state.number6 } onClick={() => this.login()} className="dynamic-font-normal text-bold">CONTINUE</Button>
                </Col>
              </Row>
        </div>
    );
  }
}

export default withRouter(LoginForm);