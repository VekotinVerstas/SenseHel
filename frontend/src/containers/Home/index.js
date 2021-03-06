import React, { Component } from 'react';
import moment from 'moment';
import './home.styles.css';
import AppHeader from '../../components/AppHeader';
import SensorValueCard from '../../components/SensorValueCard';
import SubscribedServiceCard from '../../components/SubscribedServiceCard';
import NoSubscriptionsCard from '../../components/NoSubscriptionsCard';
import PullToRefresh from '../../components/PullToRefresh';
import API from '../../services/Api';
import CustomizedSnackbar from '../../components/Snackbar';
import LocalStorageKeys from '../../config/LocalStorageKeys';
import SensorConfig from '../../config/SensorConfig';

class HomePage extends Component {
  state = {
    subscribedServices: [],
    refreshing: false,
    errorMessage: '',
    name: '',
    address: '',
    sensorValues: []
  };

  async componentDidMount() {
    this.updateName();
    await this.fetchApartment();
    await this.fetchSubscribedServices();
    await this.fetchSensorValues();

    this.sensorValuesInterval = setInterval(
      this.fetchSensorValues,
      15 * 60 * 1000
    );
  }

  componentWillUnmount() {
    clearInterval(this.sensorValuesInterval);
  }

  updateName = () => {
    const currentUser = JSON.parse(
      localStorage.getItem(LocalStorageKeys.CURRENT_USER)
    );
    const name = `${currentUser.first_name} ${currentUser.last_name}`;
    this.setState({ name });
  };

  fetchSubscribedServices = async () => {
    try {
      const subscribedServices = await API.getSubscribedServices();

      this.setState({ subscribedServices });
    } catch (e) {
      this.setState({
        errorMessage: {
          title: 'Could not fetch subscribed services',
          subtitle: `${e.message}`
        }
      });
    }
  };

  fetchApartment = async () => {
    try {
      const apartment = await API.getApartment();
      const address = `${apartment.street}\n${apartment.city}`;
      this.setState({ address });
    } catch (e) {
      this.setState({
        errorMessage: {
          title: 'Could not fetch address',
          subtitle: `${e.message}`
        }
      });
    }
  };

  fetchSensorValues = async () => {
    try {
      const sensorValues = await API.getApartmentSensors();

      this.setState({ sensorValues });
    } catch (e) {
      this.setState({
        errorMessage: {
          title: 'Could not fetch sensor values',
          subtitle: `${e.message}`
        }
      });
    }
  };

  handleChangeTab = () => {
    const { changeTab } = this.props;
    setTimeout(() => changeTab(1), 800);
  };

  onRefresh = () =>
    new Promise(async resolve => {
      await this.fetchSubscribedServices();
      await this.fetchApartment();
      setTimeout(resolve, 1000);
    });

  render() {
    const {
      subscribedServices,
      refreshing,
      errorMessage,
      name,
      address,
      sensorValues
    } = this.state;

    return (
      <PullToRefresh onRefresh={this.onRefresh}>
        <div className="home-page">
          <AppHeader headline={name} title={address} hasBgImage />

          <div className="home-page__content tab-page__content">
            <div className="home-page__cards-container">
              {sensorValues.map(s => {
                const sensorConfig =
                  SensorConfig[s.uiType] || SensorConfig.DEFAULT;
                const lastUpdated =
                  s.updatedAt && moment(s.updatedAt).fromNow();

                return (
                  <SensorValueCard
                    key={s.id}
                    title={s.name}
                    icon={sensorConfig.getSeverityIcon(s.value)}
                    unit={sensorConfig.unit}
                    value={s.value}
                    lastUpdated={lastUpdated}
                    refreshing={refreshing}
                  />
                );
              })}
            </div>

            <div className="home-page__subscriptions-container">
              <p className="title dark-text left-aligned home-page__subscription-title">
                subscriptions
              </p>

              {subscribedServices.length > 0 ? (
                subscribedServices.map(({ service: s }) => (
                  <SubscribedServiceCard
                    key={s.name}
                    logo={s.img_logo_url}
                    title={s.name}
                    description={s.description}
                    serviceImage={s.img_service_url}
                    url={s.link}
                  />
                ))
              ) : (
                <NoSubscriptionsCard onClick={this.handleChangeTab} />
              )}
            </div>
          </div>

          <CustomizedSnackbar
            message={errorMessage}
            variant="error"
            handleClose={() => this.setState({ errorMessage: '' })}
            open={!!errorMessage}
          />
        </div>
      </PullToRefresh>
    );
  }
}

export default HomePage;
