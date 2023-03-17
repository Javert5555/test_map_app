import {
    // interaction, custom, control, //name spaces
    // Interactions, Overlays, Controls, Overlay, Util,    //group
    Map, Layers, layer    //objects
} from "react-openlayers";

const MapComponent = () => {
    return (
        <div className="map-component">
            <Map view={{center: [0,0], zoom: 2}}>
                <Layers>
                    <layer.Tile></layer.Tile>
                </Layers>
            </Map>
        </div>
    )
}

export default MapComponent