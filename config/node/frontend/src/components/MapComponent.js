import React, {useEffect, useRef} from 'react';
import Map from "ol/Map";
import TileLayer from "ol/layer/Tile";
import {OSM} from "ol/source";
import {View} from "ol";
import {useGeographic} from "ol/proj";
import 'ol/ol.css';

function MapComponent(props) {
    const mapRef = useRef(null);
    useGeographic();
    useEffect(() => {
        const map = new Map({
            target: mapRef.current,
            layers:[
                new TileLayer({
                    source: new OSM(),
                })
            ],
            view: new View({
                center: [21, 51],
                zoom: 6
            })
        })
        return () => map.setTarget(null)
    },
        []);

    return (
        <div className='MapComponent' ref={mapRef}>
        </div>
    );
}

export default MapComponent;