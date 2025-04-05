<template>
    <div class="main-container">
      <div class="top-navigation">
        <div class="status-bar">
          <div class="left-side">
            <div class="status-bar-time"><span class="time">9:41</span></div>
          </div>
          <div class="dynamic-island">
            <div class="status-bar-dynamic-island">
              <div class="true-depth-camera"></div>
              <div class="facetime-camera"></div>
            </div>
          </div>
          <div class="right-side">
            <div class="signal-wifi-battery">
              <div class="icon-mobile-signal"></div>
              <div class="wifi"></div>
              <div class="status-bar-battery"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="frame">
        <div class="frame-1" @click="goshop"><div class="vector"></div></div>
        <span class="details">Details</span>
        <div class="frame-2">
          <div class="frame-3">
            <div class="ellipse"></div>
            <div class="ellipse-4"></div>
            <div class="ellipse-5"></div>
          </div>
        </div>
      </div>
      <div class="mask-group"></div>
      <span class="try-snapchat-plus">try snapchat+for $1.99/mol</span
      ><span class="three-months-offer"
        >3 months for $1.99/mounth,then $1.99?mo!</span
      >
      <div class="rectangle">
        <div class="flex-column-ecb">
          <span class="first-three-months">$1.99/mo for the first 3 months</span
          ><span class="first-three-months-6"
            >$1.99/mo for the first 3 months</span
          ><span class="monthly-plan">monthly plan</span>
          <div class="frame-7"><span class="save-50-percent">save 50%</span></div>
        </div>
        <div class="frame-8"><div class="tick-mark"></div></div>
      </div>
      <div class="rectangle-9">
        <div class="flex-column-e">
          <span class="first-months">$1.99/mo for the first 3 months</span
          ><span class="first-months-a">$1.99/mo for the first 3 months</span
          ><span class="monthly-plan-b">monthly plan</span>
          <div class="frame-c"><span class="save-percent">save 50%</span></div>
        </div>
        <div class="frame-d"><div class="checkmark"></div></div>
      </div>
      <div class="rectangle-e">
        <div class="flex-column-a">
          <span class="first-months-f">$1.99/mo for the first 3 months</span
          ><span class="first-three-months-10"
            >$1.99/mo for the first 3 months</span
          ><span class="monthly-plan-11">monthly plan</span>
          <div class="frame-12">
            <span class="save-50-percent-13">save 50%</span>
          </div>
        </div>
        <div class="frame-14"><div class="checkmark-15"></div></div>
      </div>
      <div class="frame-16"><span class="subscribe">subscribe</span></div>
      <div class="home-indicator"></div>
      <div class="rectangle-17"></div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goshop = () => {
  router.push({ name: 'shop' });
};
</script>
  
  <style scoped>
:root {
  --default-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Ubuntu, "Helvetica Neue", Helvetica, Arial, "PingFang SC",
    "Hiragino Sans GB", "Microsoft Yahei UI", "Microsoft Yahei",
    "Source Han Sans CN", sans-serif;
}

.main-container {
  overflow: hidden;
}

.main-container,
.main-container * {
  box-sizing: border-box;
}

input,
select,
textarea,
button {
  outline: 0;
}

.main-container {
  position: relative;
  width: 393px;
  height: 852px;
  margin: 0 auto;
  background: #1d1e20;
  overflow: hidden;
}
.top-navigation {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 393px;
  margin: 0 0 0 0;
  background: #1d1e20;
  backdrop-filter: blur(10px);
}
.status-bar {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 59px;
  z-index: 1;
}
.left-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 0 3px 10px;
  z-index: 2;
}
.status-bar-time {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 3;
  border-radius: 24px;
}
.time {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 54px;
  height: 20px;
  top: 1px;
  left: 0;
  color: #ffffff;
  font-family: SF Pro Text, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 4;
}
.dynamic-island {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  width: 125px;
  min-height: 0;
  z-index: 5;
}
.status-bar-dynamic-island {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
  border-radius: 100px;
}
.true-depth-camera {
  position: absolute;
  width: 80px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(-78.13%, -50%);
  z-index: 7;
  overflow: hidden;
  border-radius: 100px;
}
.facetime-camera {
  position: absolute;
  width: 37px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(68.92%, -50%);
  z-index: 8;
  overflow: hidden;
  border-radius: 100px;
}
.right-side {
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 11px 0 0;
  z-index: 9;
}
.signal-wifi-battery {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 10;
}
.icon-mobile-signal {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/wifi-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 12;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.frame {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 94px;
  position: relative;
  width: 351px;
  height: 52px;
  margin: 11px 0 0 21px;
  z-index: 18;
}
.frame-1 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 51px;
  height: 51px;
  padding: 19px 21px 19px 21px;
  background: #ffffff;
  z-index: 19;
  border-radius: 25.5px;
}
.vector {
  flex-shrink: 0;
  position: relative;
  width: 11px;
  height: 15px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/back-arrow.svg)
    no-repeat center;
  background-size: cover;
  z-index: 20;
}
.details {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 61px;
  height: 22px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 600;
  line-height: 21.784px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 21;
}
.frame-2 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 51px;
  height: 51px;
  padding: 13px 24px 13px 24px;
  background: #ffffff;
  z-index: 22;
  border-radius: 25.5px;
}
.frame-3 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 3px;
  position: relative;
  width: 3px;
  z-index: 23;
}
.ellipse {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/ellipse-dot-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 24;
  border-radius: 50%;
}
.ellipse-4 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/ellipse-dot-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 25;
  border-radius: 50%;
}
.ellipse-5 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/ellipse-dot-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 26;
  border-radius: 50%;
}
.mask-group {
  position: relative;
  width: 176.676px;
  height: 75.484px;
  margin: 53.068px 0 0 107.95px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/snapchat-logo.png)
    no-repeat center;
  background-size: cover;
  z-index: 27;
}
.try-snapchat-plus {
  display: block;
  position: relative;
  height: 22px;
  margin: 53.448px 0 0 69px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 500;
  line-height: 21.784px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 16;
}
.three-months-offer {
  display: block;
  position: relative;
  height: 15px;
  margin: 7px 0 0 53px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 500;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: 0.48px;
  opacity: 0.5;
  z-index: 17;
}
.rectangle {
  position: relative;
  width: 367.848px;
  height: 105.069px;
  margin: 17.825px 0 0 13.624px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/subscription-card-1.png)
    no-repeat center;
  background-size: cover;
  z-index: 29;
  border-radius: 17px;
}
.flex-column-ecb {
  position: absolute;
  height: 73.446px;
  top: 12.241px;
  right: 83.84px;
  left: 22.008px;
  font-size: 0px;
  z-index: 35;
}
.first-three-months {
  display: block;
  position: relative;
  height: 19.382px;
  margin: 30.603px 0 0 0;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 16px;
  font-weight: 500;
  line-height: 19.364px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 31;
}
.first-three-months-6 {
  display: block;
  position: relative;
  height: 15.301px;
  margin: 8.16px 0 0 0;
  color: #989898;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 500;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: 0.48px;
  z-index: 32;
}
.monthly-plan {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22.442px;
  top: 0;
  left: calc(50% - 131px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 500;
  line-height: 21.784px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 30;
}
.frame-7 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 59.736px;
  height: 21.422px;
  top: 1.02px;
  left: 131px;
  padding: 4px 5px 4px 5px;
  background: linear-gradient(135deg, #fcefa9, #e5af4d);
  z-index: 35;
  border-radius: 3px;
}
.save-50-percent {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 12px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 9.818181991577148px;
  font-weight: 600;
  line-height: 11.882px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 36;
}
.frame-8 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 48.208px;
  height: 46.924px;
  top: 29.583px;
  left: 301.824px;
  padding: 4px 4px 4px 4px;
  background: #252525;
  z-index: 33;
  border-radius: 23px;
}
.tick-mark {
  flex-shrink: 0;
  position: relative;
  width: 37px;
  height: 37px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/tick-mark-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 34;
  overflow: hidden;
}
.rectangle-9 {
  position: relative;
  width: 367.848px;
  height: 105.069px;
  margin: 16.321px 0 0 13.624px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/subscription-card-2.png)
    no-repeat center;
  background-size: cover;
  z-index: 38;
  border-radius: 17px;
}
.flex-column-e {
  position: absolute;
  height: 73.446px;
  top: 12.241px;
  right: 83.84px;
  left: 22.008px;
  font-size: 0px;
  z-index: 44;
}
.first-months {
  display: block;
  position: relative;
  height: 19.382px;
  margin: 30.603px 0 0 0;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 16px;
  font-weight: 500;
  line-height: 19.364px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 40;
}
.first-months-a {
  display: block;
  position: relative;
  height: 15.301px;
  margin: 8.16px 0 0 0;
  color: #989898;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 500;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: 0.48px;
  z-index: 41;
}
.monthly-plan-b {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22.442px;
  top: 0;
  left: calc(50% - 131px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 500;
  line-height: 21.784px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 39;
}
.frame-c {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 59.736px;
  height: 21.422px;
  top: 1.02px;
  left: 131px;
  padding: 4px 5px 4px 5px;
  background: linear-gradient(135deg, #fcefa9, #e5af4d);
  z-index: 44;
  border-radius: 3px;
}
.save-percent {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 12px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 9.818181991577148px;
  font-weight: 600;
  line-height: 11.882px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 45;
}
.frame-d {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 48.208px;
  height: 46.924px;
  top: 29.583px;
  left: 301.824px;
  padding: 4px 4px 4px 4px;
  background: #252525;
  z-index: 42;
  border-radius: 23px;
}
.checkmark {
  flex-shrink: 0;
  position: relative;
  width: 37px;
  height: 37px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/checkmark-icon-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 43;
  overflow: hidden;
}
.rectangle-e {
  position: relative;
  width: 367.848px;
  height: 105.069px;
  margin: 16.322px 0 0 13.624px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/subscription-card-3.png)
    no-repeat center;
  background-size: cover;
  z-index: 47;
  border-radius: 17px;
}
.flex-column-a {
  position: absolute;
  height: 73.446px;
  top: 12.241px;
  right: 83.84px;
  left: 22.008px;
  font-size: 0px;
  z-index: 53;
}
.first-months-f {
  display: block;
  position: relative;
  height: 19.382px;
  margin: 30.603px 0 0 0;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 16px;
  font-weight: 500;
  line-height: 19.364px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 49;
}
.first-three-months-10 {
  display: block;
  position: relative;
  height: 15.301px;
  margin: 8.16px 0 0 0;
  color: #989898;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 500;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: 0.48px;
  z-index: 50;
}
.monthly-plan-11 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22.442px;
  top: 0;
  left: calc(50% - 131px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 500;
  line-height: 21.784px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 48;
}
.frame-12 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 59.736px;
  height: 21.422px;
  top: 1.02px;
  left: 131px;
  padding: 4px 5px 4px 5px;
  background: linear-gradient(135deg, #fcefa9, #e5af4d);
  z-index: 53;
  border-radius: 3px;
}
.save-50-percent-13 {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 12px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 9.818181991577148px;
  font-weight: 600;
  line-height: 11.882px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 54;
}
.frame-14 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 48.208px;
  height: 46.924px;
  top: 29.583px;
  left: 301.824px;
  padding: 4px 4px 4px 4px;
  background: #252525;
  z-index: 51;
  border-radius: 23px;
}
.checkmark-15 {
  flex-shrink: 0;
  position: relative;
  width: 37px;
  height: 37px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/checkmark-icon-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 52;
  overflow: hidden;
}
.frame-16 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 65px;
  position: relative;
  width: 350px;
  height: 60px;
  margin: 14.326px 0 0 22px;
  padding: 5px 6px 5px 6px;
  background: #ff5218;
  z-index: 56;
  border-radius: 29.5px;
}
.subscribe {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 99px;
  height: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 500;
  line-height: 24.747px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 57;
}
.home-indicator {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 51px 0 0 130px;
  background: #000000;
  z-index: 15;
  border-radius: 100px;
}
.rectangle-17 {
  position: absolute;
  width: 393px;
  height: 43px;
  top: 671px;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185156/bottom-gradient.png)
    no-repeat center;
  background-size: cover;
  z-index: 55;
}

</style>
  