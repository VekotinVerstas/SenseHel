import React from 'react';
import CircularProgress from '@material-ui/core/CircularProgress/CircularProgress';
import './sensorvaluecard.styles.css';

const SensorValueCard = ({
  title,
  icon,
  unit,
  value,
  lastUpdated,
  refreshing
}) => (
  <div className="service-card">
    <div className="service-card__header">
      <span className="body-text">{title}</span>
      <img className="service-card__header__icon" src={icon} alt={title} />
    </div>

    {!refreshing ? (
      <div>
        <span className="large-number">
          {value}
          <span className="number">{unit}</span>
        </span>
      </div>
    ) : (
      <CircularProgress className="service-card__spinner" />
    )}

    <div className="small-body">
      {!refreshing ? `Updated ${lastUpdated}` : 'Refreshing'}
    </div>
  </div>
);

export default SensorValueCard;
