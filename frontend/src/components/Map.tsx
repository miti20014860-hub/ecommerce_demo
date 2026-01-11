import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import type { MapContainerProps } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';


L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
  iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
});

interface MapProps extends MapContainerProps {
  lat: number | string;
  lng: number | string;
  address?: string;
  zoom?: number;
  height?: string;
  mapId?: string;
}

export default function Map({
  lat,
  lng,
  address = '位置',
  zoom = 15,
  height = '400px',
  mapId = 'map',
  ...rest
}: MapProps) {
  const latitude = Number(lat);
  const longitude = Number(lng);

  if (isNaN(latitude) || isNaN(longitude)) {
    return (
      <div className="w-full bg-red-100 text-red-700 p-4 rounded-lg" style={{ height }}>
        無效的經緯度資料
      </div>
    );
  }

  const position: [number, number] = [latitude, longitude];

  return (
    <div className="w-full rounded-lg overflow-hidden" style={{ height }} id={mapId}>
      <MapContainer
        center={position}
        zoom={zoom}
        scrollWheelZoom={false}
        className="h-full"
        {...rest}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker position={position}>
          <Popup>{address}</Popup>
        </Marker>
      </MapContainer>
    </div>
  );
}