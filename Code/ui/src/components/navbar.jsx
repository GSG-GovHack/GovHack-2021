import React from 'react';
import { Navbar, Button, Alignment, Dialog, Classes, NumericInput, FormGroup } from '@blueprintjs/core'

class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            locationEnterBox: false,
            lat: props.location[0],
            lon: props.location[1]
        }
    }

    getLocation = () => {
        if (!navigator.geolocation) {
            alert('Geolocation is not supported by your browser :(');
        } else {
            navigator.geolocation.getCurrentPosition((position) => {
                this.props.globalStateHandler({ location: [position.coords.latitude, position.coords.longitude] })
                this.props.updateGeoJsonData();
            }, () => {
                alert('Unable to retrieve your location :(');
            });
        }
    }

    enterLocation = () => this.setState({ locationEnterBox: true })
    close = () => this.setState({ locationEnterBox: false })
    updateLat = (val, valAsStr, element) => this.setState({ lat: val })
    updateLon = (val, valAsStr, element) => this.setState({ lon: val })
    saveLocation = () => {
        this.props.globalStateHandler({ location: [this.state.lat, this.state.lon]});
        this.props.updateGeoJsonData();
        this.close();
    }

    render() {
        return (
            <div>
                <Navbar>
                    <Navbar.Group align={Alignment.LEFT}>
                        <Navbar.Heading>Project Clover</Navbar.Heading>
                        <Navbar.Divider />
                        <Button className="bp3-minimal" icon="home" text="Home" />
                        <Button className="bp3-minimal" icon="geolocation" text="Locate Me" onClick={this.getLocation} />
                        <Button className="bp3-minimal" icon="geolocation" text="(Testing) Enter Fake Location" onClick={this.enterLocation} />
                    </Navbar.Group>
                </Navbar>
                <Dialog isOpen={this.state.locationEnterBox} usePortal={true} title="Enter Location" onClose={this.close}>
                    <div className={Classes.DIALOG_BODY}>
                        <p>Please enter your location</p>
                    </div>
                    <div className={Classes.DIALOG_FOOTER}>
                        <FormGroup label="Latitude">
                            <NumericInput value={this.state.lat} onValueChange={this.updateLat} min={-90} max={90} />
                        </FormGroup>
                        <FormGroup label="Longitude">
                            <NumericInput value={this.state.lon} onValueChange={this.updateLon} min={0} max={180}/>
                        </FormGroup>

                        <div className={Classes.DIALOG_FOOTER_ACTIONS}>
                            <Button intent="success" onClick={this.saveLocation}>Go!</Button>
                            <Button onClick={this.close}>Close</Button>
                        </div>
                    </div>

                </Dialog>
            </div>
        )
    }
}

export default NavBar;