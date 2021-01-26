<table>
  <tr>
    <td> <img src="image/fig1.png" alt="1" width = 360px height = 640px> </td>
    <td> <img src="image/fig2.png" alt="2" width = 360px height = 640px> </td>
   </tr> 
   <tr>
    <td> <img src="image/fig3.png" alt="3" width = 360px height = 640px> </td>
    <td> <img src="image/fig4.png" alt="4" width = 360px height = 640px> </td>
  </tr>
  <tr>
  	<td> <img src="image/fig5.png" alt="5" width = 360px height = 640px> </td>
  </tr>
</table>


```matlab
% ****************
% * Windowing.m (Lab 1)*
% ****************

fs = 4; % Sampling rate in [kHz].
        % It determines the range of frequencies for which the spectrum
        % is computed by the Fourier transform function 'fft' used below.
        % The spectrum is computed for the range [-fs/2,fs/2[
Ts = 1/fs; % Sampling interval in [ms]

% ****************
% * First Window *
% ****************
WindowLength1 = 10; % 10ms window, 2*T1 = WindowLength, T1 = 0.005sec

t = -WindowLength1/2:Ts:WindowLength1/2-Ts; % sampled time base
f1 = 0.5; % Frequency component, in [kHz]
omega = 2*pi*f1;

% Complex exponential
% *******************
x0 = exp(j*omega*t);
NPoints = 2000; % Number of points used to compute the Fourier transform
X0 = fft(x0,NPoints); % Using MATLAB Fourier transform function 'fft' to compute spectrum
X0 = fftshift(X0); % Arranging fft output to have 0Hz in the center.
f = -fs/2:fs/NPoints:fs/2-fs/NPoints; % Frequency range [-fs/2,fs/2[ for which
                                      % the fft computes the spectrum X1(j*omega)
figure(1)
clf; plot(f,abs(X0),'b'); xlabel('freq [kHz]'); grid on; zoom on
ylabel('|H(j\omega)|')
title(['Magnitude spectrum of a ' num2str(f1) 'kHz complex exponential over a ' ...
        num2str(WindowLength1) ' ms window'])

% Cosine
% ******
x1 = cos(omega*t);
figure(2)
clf; plot(t,x1,'b.-'); xlabel('time [ms]'); grid on; zoom on
title([num2str(f1) 'kHz cosine over a ' num2str(WindowLength1) 'ms window'])

X1 = fft(x1,NPoints); % Using MATLAB Fourier transform function 'fft' to compute spectrum
X1 = fftshift(X1); % Arranging fft output to have 0Hz in the center.
figure(3)
clf; plot(f,abs(X1),'b'); xlabel('freq [kHz]'); grid on; zoom on
ylabel('|H(j\omega)|')
title(['Magnitude spectrum of a ' num2str(f1) 'kHz sinusoid over a ' ...
        num2str(WindowLength1) ' ms window'])

% *****************
% * Second Window *
% *****************
WindowLength2 = 20; % 20ms window, 2*T1 = WindowLength, T1 = 0.01sec

% Cosine
% ******
t = -WindowLength2/2:Ts:WindowLength2/2-Ts; % sampled time base
f2 = 0.5; % Frequency component, in [kHz]
omega = 2*pi*f2;
x1 = cos(omega*t);
figure(4)
clf; plot(t,x1,'b.-'); xlabel('time [ms]'); grid on; zoom on
title([num2str(f2) 'kHz cosine over a ' num2str(WindowLength2) 'ms window'])

X1 = fft(x1,NPoints); % Using MATLAB Fourier transform function to compute spectrum
X1 = fftshift(X1); % Arranging fft output to have 0Hz in the center.
figure(5)
clf; plot(f,abs(X1),'b'); xlabel('freq [kHz]'); grid on; zoom on
ylabel('|H(j\omega)|')
title(['Magnitude spectrum of a ' num2str(f2) 'kHz sinusoid over a ' ...
        num2str(WindowLength2) ' ms window'])

```