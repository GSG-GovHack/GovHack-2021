import React from 'react';
import L from 'leaflet';
import { MapContainer, TileLayer, Marker, useMap, GeoJSON } from 'react-leaflet';

import '../styling/home.sass';
import NavBar from '../components/navbar';
import http from '../httplib';

function SetViewOnClick({ coords }) {
    const map = useMap();
    map.setView(coords, map.getZoom());
    return null;
}

function GetMapCenter({ stateCallback }) {
    const map = useMap()
    stateCallback(map.getCenter())
    return null;
}

const userLocationMarker = new L.Icon({
    iconUrl: require('../img/red.png').default,
    iconAnchor: null,
    popupAnchor: null,
    shadowUrl: null,
    shadowSize: null,
    shadowAnchor: null,
    markerColor: 'transparent',
    iconSize: new L.Point(30, 30),

})

class HomePage extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            points: 0,
            location:           [-31.95, 115.86],
            defaultLocation:    [-31.95, 115.86],
            center:             [-31.95, 115.86],
            geojson: null,
        }
    }

    setStateWrapper = (newstate) => {
        this.setState(newstate)
    }

    getDefaultCenter = () => {
        if (this.state.location === null) {
            return this.state.defaultLocation;
        } else {
            return this.state.location
        }
    }

    LocationMarker = () => {
        if (this.state.location !== null) {
            return (
                <Marker icon={userLocationMarker} position={this.state.location}>
                </Marker>
            )
        } else {
            return null;
        }
    }

    getGeoJSON = () => {
        if (this.state.location !== null) {
            http.get(`/places/${this.state.location[0]}/${this.state.location[1]}`)
                .then((response) => {
                    this.setState({ geojson: response.data })
                    console.log(response.data)
                })
                .catch((error) => {
                    console.log(error)
                    return null;
                })
            return null;
        } else {
            return null;
        }
    }

    updateCoords = (coords) => {
        this.setState({ center: [coords.lat, coords.lon] })
        return null;
    }
    updateGeoJSONData = () => this.getGeoJSON()

    componentDidMount = () => {
        this.getGeoJSON()
    }

    renderGeoJSON = () => {
        if (this.state.geojson !== null) {
            return (
                <GeoJSON data={this.state.geojson}></GeoJSON>
            )
        }
    }

    render() {
        return (
            <div>
                <NavBar state={this.state} globalStateHandler={this.setStateWrapper} location={this.getDefaultCenter()} updateGeoJsonData={this.updateGeoJSONData} />
                <MapContainer center={this.getDefaultCenter()} zoom={13} scrollWheelZoom={true} className="map" id="map">
                    <SetViewOnClick coords={this.getDefaultCenter()} />
                    <TileLayer
                        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    <this.LocationMarker />
                    {this.renderGeoJSON()}
                    {/* <GetMapCenter stateCallback={this.updateCoords} /> */}
                </MapContainer>
            </div>
        )
    }

}

export default HomePage;