import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { withRouter } from "react-router-dom";

import '../../App.css';

import {store} from '../../util/store'

class ProviderDashboard extends Component {

  constructor(props) {
    store.init();
    super(props);
    this.state = {
      currentItem: 'login'
    }
  }
  render() {
    return (
      <Container className="dashboard">
        <Row>
          <Col md="1" className="dashboard-menu">
            <div>
              <div class="dashboard-user-thumb-container">
                <div class="e0tvheqt block">
                  <div class="e0l16gps block">
                    <div class="e095srs9 block"></div>
                  </div>
                </div>
              </div>
              <div class="e0csioo8 block">
                <div class="e0g0fmr9 block">
                  <div class="e0b6a8e0 block">
                    <div class="e0okb4z3 block"></div>
                    <div class="e0gvpo4a block">
                      <div class="e0b9t1cz block"></div>
                    </div>
                    <p class="e0a0oksp text">dashboard</p>
                  </div>
                </div>
                <div class="e04emmgl block">
                  <div class="e0zdqc6n block">
                    <p class="e0kjuf4j text">Patients</p>
                  </div>
                </div>
                <div class="e0shxz4c block">
                  <div class="e08h26uu block">
                    <div class="e08pc8f9 block">
                      <div class="e0w6k1c1 block"></div>
                    </div>
                    <p class="e0h5a0ba text">Patient cases</p>
                  </div>
                </div>
                <div class="e0ydimum block">
                  <div class="e0hkv5vv block">
                    <div class="e0c96zfj block"></div>
                    <p class="e0mk00w4 text">schedule</p>
                  </div>
                </div>
                <div class="e0ug0tcn block">
                  <div class="e06tvpp6 block">
                    <p class="e0qnedqs text">appointments</p>
                  </div>
                </div>
                <div class="e0n1j48h block">
                  <div class="e058hejn block">
                    <p class="e0riidp4 text">Messages</p>
                    <div class="e0zk3xt3 block">
                      <p class="e067l9gu text">32</p>
                    </div>
                  </div>
                </div>
                <div class="e05uho0g block">
                  <div class="e05d04be block">
                    <p class="e0vwzgw6 text">RPM Templates</p>
                  </div>
                </div>
                <div class="e0sxv8w8 block">
                  <div class="e0eknu8w block">
                    <p class="e0dudrue text">Billing</p>
                  </div>
                </div>
                <div class="e02xemgz block">
                  <div class="e0ux49kt block">
                    <p class="e0i7d918 text">administration</p>
                  </div>
                </div>
                <div class="e0pqeohn block">
                  <div class="e00xanpz block">
                    <p class="e07ntajp text">Analytics</p>
                  </div>
                </div>
              </div>
            </div>
          </Col>
          <Col md="11" className="dashboard-content">
            <Row>
              <Col>
                
              </Col>
            </Row>

            <Row>
              <Col>
                
              </Col>
            </Row>

            <Row>
              <Col>

              </Col>
            </Row>


            <Row>
              <Col>
                
              </Col>
            </Row>
          
          </Col>
        </Row>
      </Container>
    );
  }
}

export default withRouter(ProviderDashboard);