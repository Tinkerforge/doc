program Example;

{$ifdef MSWINDOWS}{$apptype CONSOLE}{$endif}
{$ifdef FPC}{$mode OBJFPC}{$H+}{$endif}

uses
  SysUtils, IPConnection;

type
  TExample = class
  private
    ipcon: TIPConnection;
  public
    procedure EnumerateCB(const uid: string; const name: string; 
                          const stackID: byte; const isNew: boolean);
    procedure Execute;
  end;

const
  HOST = 'localhost';
  PORT = 4223;

var
  e: TExample;

procedure TExample.EnumerateCB(const uid: string; const name: string; 
                               const stackID: byte; const isNew: boolean);
begin
  if (isNew) then begin
    WriteLn('New Device:');
  end
  else begin
    WriteLn('Device Removed:');
  end;
  WriteLn(' Name:     ' + name);
  WriteLn(' UID:      ' + uid);
  WriteLn(' Stack ID: ' + IntToStr(stackID));
  WriteLn('');
end;

procedure TExample.Execute;
begin
  { Create IP connection to brickd }
  ipcon := TIPConnection.Create(HOST, PORT);

  { Enumerate Bricks and Bricklets }
  ipcon.Enumerate({$ifdef FPC}@{$endif}self.EnumerateCB);

  WriteLn('Press key to exit');
  ReadLn;
  ipcon.Destroy;
end;

begin
  e := TExample.Create;
  e.Execute;
  e.Destroy;
end.
